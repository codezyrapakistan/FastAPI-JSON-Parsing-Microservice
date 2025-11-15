from fastapi import FastAPI
from app.api.routes_sbom import router as sbom_router
from app.core.config import settings
from motor.motor_asyncio import AsyncIOMotorClient
import app.core.config as config

app = FastAPI(
    title="FastAPI SBOM Checker",
    description="Analyze SBOM JSON files and enrich with OSV vulnerability data",
    version="1.0.0",
)

@app.on_event("startup")
async def startup_event():
    print("Connecting to MongoDB...")
    config.client = AsyncIOMotorClient(settings.MONGO_URI)
    config.db = config.client[settings.DB_NAME]
    print("MongoDB Connected Successfully!")

@app.on_event("shutdown")
async def shutdown_event():
    config.client.close()

app.include_router(sbom_router, prefix="/api", tags=["SBOM"])

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to SBOM Checker API"}
