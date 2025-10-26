from __future__ import annotations

from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def _heading_lines(markdown: str) -> list[str]:
    return [line.strip() for line in markdown.splitlines() if line.strip().startswith("#")]


def _duplicate_headings(headings: list[str]) -> set[str]:
    counts = Counter(headings)
    return {heading for heading, occurrences in counts.items() if occurrences > 1}


def _primary_heading(markdown: str) -> str | None:
    for line in markdown.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped
    return None


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


def test_adr_headings_unique() -> None:
    adr_dir = REPO_ROOT / "docs" / "adr"
    seen_headings: dict[str, str] = {}
    duplicates: dict[str, list[str]] = {}

    for adr_file in sorted(adr_dir.glob("*.md")):
        content = adr_file.read_text(encoding="utf-8")
        heading = _primary_heading(content)
        relative_name = adr_file.relative_to(REPO_ROOT).as_posix()

        assert heading is not None, f"Brak nagłówka tytułu w {relative_name}"

        if heading in seen_headings:
            duplicates.setdefault(heading, [seen_headings[heading]]).append(relative_name)
        else:
            seen_headings[heading] = relative_name

    assert not duplicates, f"Zduplikowane tytuły ADR: {duplicates}"
