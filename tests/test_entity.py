import pytest

from capycalypse.logic.entity import Entity


def test_entity_stores_position_and_size():
    entity = Entity(10, 20, 30, 40)

    assert (entity.x, entity.y) == (10, 20)
    assert (entity.width, entity.height) == (30, 40)
    assert entity.active is True


def test_entity_update_must_be_overridden():
    entity = Entity(0, 0, 1, 1)

    with pytest.raises(NotImplementedError):
        entity.update()
