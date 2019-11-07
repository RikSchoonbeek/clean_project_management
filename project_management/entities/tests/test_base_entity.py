from ..base import BaseEntity


class NonABCBaseEntity(BaseEntity):
    pass


def test_generate_unique_id_default():
    instance = NonABCBaseEntity()

    assert type(instance.id) is str
    assert len(instance.id) == 7
    assert instance.id is instance._id


def test_generate_unique_id_custom_length():
    instance = NonABCBaseEntity(id_length=10)

    assert type(instance.id) is str
    assert len(instance.id) == 10
