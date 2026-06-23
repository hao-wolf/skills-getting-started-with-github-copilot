import copy
import pytest
from fastapi.testclient import TestClient
from src.app import app, activities


@pytest.fixture
def client():
    # Arrange: snapshot the in-memory activities so tests don't interfere
    original = copy.deepcopy(activities)
    with TestClient(app) as c:
        yield c
    # Teardown: restore original activities state
    activities.clear()
    activities.update(original)
