from .base import BaseEntity


class UnitOfWork(BaseEntity):

    def __init__(self, description, project_id, result, title):
        super().__init__()
        self._description = description
        self._project_id = project_id
        self._result = result
        self._title = title
