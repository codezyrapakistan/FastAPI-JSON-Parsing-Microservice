import httpx
from typing import List
from app.models.sbom_models import Component

async def query_osv(components: List[Component]):
    payload = {
        "queries": [
            {"package": {"name": c.name}, "version": c.version or ""}
            for c in components
        ]
    }
    async with httpx.AsyncClient() as client:
        r = await client.post("https://api.osv.dev/v1/querybatch", json=payload)
        r.raise_for_status()
        data = r.json()

    results = []
    for c, vulns in zip(components, data.get("results", [])):
        results.append({
            "name": c.name,
            "version": c.version,
            "license": c.license,
            "vulnerability_count": len(vulns.get("vulns", []))
        })
    return results
