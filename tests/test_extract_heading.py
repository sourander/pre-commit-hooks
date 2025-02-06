import pytest

from pre_commit_hooks.extract_exercise_list import extract_heading
from pathlib import Path

@pytest.fixture
def heading_01():
    return Path("tests/data/extract_heading_01.md").read_text()

@pytest.fixture
def heading_02():
    return Path("tests/data/extract_heading_02.md").read_text()

def test_extract_heading(heading_01):
    expected = "🐳 Tämä on otsikko"
    assert extract_heading(heading_01) == expected

def test_extract_no_heading(heading_02):
    expected = "No heading found"
    assert extract_heading(heading_02) == expected