import json
from app.models.sbom_models import Component

def parse_sbom_json(raw_data: str):
    """Parse a raw SBOM JSON string into a list of Component objects."""
    data = json.loads(raw_data)
    components = [
        Component(
            name=item.get("name"),
            version=item.get("version"),
            license=item.get("license")
        )
        for item in data.get("components", [])
    ]
    return components
