import os

class Settings:
    APP_NAME: str = "FastAPI SBOM Checker"
    OSV_API_URL: str = "https://api.osv.dev/v1/querybatch"
    DEBUG: bool = True

settings = Settings()
