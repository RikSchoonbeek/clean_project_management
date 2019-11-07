from abc import ABC
from uuid import uuid4


class BaseEntity(ABC):

    @classmethod
    def _generate_unique_id(cls, length=7):
        return uuid4().hex
