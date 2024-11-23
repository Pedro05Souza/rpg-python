import pytest
from unittest.mock import patch
from entities.enemy import Enemy
from gamehandler import enemy_creator
from copy import deepcopy

@pytest.fixture
def enemy() -> Enemy:
    return deepcopy(enemy_creator(1))