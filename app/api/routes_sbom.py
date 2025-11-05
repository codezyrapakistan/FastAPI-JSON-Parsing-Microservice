from fastapi import APIRouter, HTTPException
from app.models.sbom_models import SBOMRequest
from app.services.osv_service import query_osv

router = APIRouter()

@router.post("/analyze")
async def analyze_sbom(sbom: SBOMRequest):
    try:
        results = await query_osv(sbom.components)
        return {"status": "success", "results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
