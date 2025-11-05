from fastapi import FastAPI
from app.api.routes_sbom import router as sbom_router

app = FastAPI(
    title="FastAPI SBOM Checker",
    description="Analyze SBOM JSON files and enrich with OSV vulnerability data",
    version="1.0.0",
)

app.include_router(sbom_router, prefix="/api", tags=["SBOM"])

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to SBOM Checker API"}
