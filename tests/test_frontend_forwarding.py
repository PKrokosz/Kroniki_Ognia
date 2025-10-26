from pathlib import Path


ASSET_PATH = Path('assets/idea-form.js')


def test_production_webhook_forwarding_script():
    content = ASSET_PATH.read_text(encoding='utf-8')

    assert 'https://juaateipzyafdyrf2kdgdlyh.hooks.n8n.cloud/webhook/_health' in content
    assert "source: 'github-pages'" in content or 'source: "github-pages"' in content
    assert 'async function submitIdea' in content
    assert 'mode: \'cors\'' in content or 'mode: "cors"' in content
