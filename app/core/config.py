import os
from motor.motor_asyncio import AsyncIOMotorClient

class Settings:
    APP_NAME: str = "FastAPI SBOM Checker"
    OSV_API_URL: str = "https://api.osv.dev/v1/querybatch"
    DEBUG: bool = True
    MONGO_URI: str = "mongodb://localhost:27017"
    DB_NAME: str = "sbom_db"

settings = Settings()
db = None   # <-- IMPORTANT
client = None