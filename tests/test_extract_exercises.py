import pytest

from pre_commit_hooks.extract_exercise_list import extract_exercises
from pathlib import Path


@pytest.fixture
def exercises_01():
    return Path("tests/data/extract_exercises_01.md").read_text()

@pytest.fixture
def exercises_02():
    return Path("tests/data/extract_exercises_02.md").read_text()


def test_extract_exercises(exercises_01):
    expected = ["Tehtävä 1: A B C a b c", "Voi olla myös Tehtävää 2"]
    assert len(extract_exercises(exercises_01)) == len(expected)

def test_extract_no_exercises(exercises_02):
    assert extract_exercises(exercises_02) == []