import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
ROOT_CONFIG = PROJECT_ROOT / "config.json"
PUBLIC_CONFIG = PROJECT_ROOT / "public" / "config.json"


def _load_config(path: Path) -> dict:
    assert path.exists(), f"Config file missing: {path}"
    data = json.loads(path.read_text())
    assert isinstance(data, dict), "Config should decode to a dictionary"
    assert data.get("BACKEND_URL"), "BACKEND_URL must be present and non-empty"
    value = data["BACKEND_URL"]
    assert isinstance(value, str), "BACKEND_URL must be a string"
    assert value.startswith("https://"), "BACKEND_URL must use https"
    assert not value.endswith("/"), "BACKEND_URL must not end with a trailing slash"
    return data


def test_root_and_public_configs_match():
    root_data = _load_config(ROOT_CONFIG)
    public_data = _load_config(PUBLIC_CONFIG)
    assert (
        root_data["BACKEND_URL"] == public_data["BACKEND_URL"]
    ), "Root and public config.json must stay synchronized"
