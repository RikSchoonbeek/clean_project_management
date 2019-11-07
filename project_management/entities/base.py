from abc import ABC
from uuid import uuid4


class BaseEntity(ABC):

    def __init__(self, id_length=None):
        self._id = self._generate_unique_id(
            length=id_length) if id_length else self._generate_unique_id()

    def _generate_unique_id(self, length=7):
        return uuid4().hex[:length]

    @property
    def id(self):
        return self._id
