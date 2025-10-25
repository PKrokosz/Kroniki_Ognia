from __future__ import annotations

from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def _heading_lines(markdown: str) -> list[str]:
    return [line.strip() for line in markdown.splitlines() if line.strip().startswith("#")]


def _duplicate_headings(headings: list[str]) -> set[str]:
    counts = Counter(headings)
    return {heading for heading, occurrences in counts.items() if occurrences > 1}


def test_readme_headings_unique() -> None:
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    headings = _heading_lines(readme)
    duplicates = _duplicate_headings(headings)
    assert not duplicates, f"Powtarzające się nagłówki w README: {sorted(duplicates)}"


def test_docs_headings_unique() -> None:
    docs = [
        REPO_ROOT / "docs" / "plan.md",
        REPO_ROOT / "docs" / "tasks.md",
        REPO_ROOT / "docs" / "notes.md",
        REPO_ROOT / "CONTEXT.md",
    ]
    problems: dict[str, list[str]] = {}
    for document in docs:
        content = document.read_text(encoding="utf-8")
        headings = _heading_lines(content)
        duplicates = sorted(_duplicate_headings(headings))
        if duplicates:
            problems[document.relative_to(REPO_ROOT).as_posix()] = duplicates
    assert not problems, f"Duplikaty nagłówków w dokumentacji: {problems}"
