import pytest

from pre_commit_hooks.extract_exercise_list import extract_priority
from pathlib import Path

@pytest.fixture
def priority_01():
    return Path("tests/data/extract_priority_01.md").read_text()

@pytest.fixture
def priority_02():
    return Path("tests/data/extract_priority_02.md").read_text()

def test_extract_priority(priority_01):
    expected = 42
    assert extract_priority(priority_01) == expected

def test_extract_no_priority(priority_02):
    expected = 999
    assert extract_priority(priority_02) == expected