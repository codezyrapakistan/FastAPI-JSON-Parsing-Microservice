from fastapi import APIRouter, HTTPException
from app.models.sbom_models import SBOMRequest
from app.services.osv_service import query_osv
import app.core.config as config   # <-- FIX

router = APIRouter()

@router.post("/analyze")
async def analyze_sbom(sbom: SBOMRequest):
    try:
        # Step 1: Get OSV API results
        results = await query_osv(sbom.components)

        # Step 2: Save to MongoDB
        record = {
            "components": [c.dict() for c in sbom.components],
            "results": results
        }

        insert_result = await config.db["sbom_reports"].insert_one(record)

        return {
            "status": "success",
            "inserted_id": str(insert_result.inserted_id),
            "results": results
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
