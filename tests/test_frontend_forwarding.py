from pathlib import Path


ASSET_PATH = Path('assets/idea-form.js')


def test_production_webhook_forwarding_script():
    content = ASSET_PATH.read_text(encoding='utf-8')

    assert 'https://submission-belt-pill-donors.trycloudflare.com/webhook/f11f16e1-4e7e-4fa6-b99e-bf1e47f02a50' in content
    assert "source: 'github-pages'" in content or 'source: "github-pages"' in content
    assert 'async function submitIdea' in content
    assert 'mode: \'cors\'' in content or 'mode: "cors"' in content
