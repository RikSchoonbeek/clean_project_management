from .base import BaseEntity


class Actor(BaseEntity):

    def __init__(self, name):
        super().__init__()
        self._name = name
