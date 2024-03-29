from .base import BaseEntity


class Project(BaseEntity):
    """
    Projects are any specific result that needs to be achieved, requiring specific 
    things that need to be done (units of work).
    """

    def __init__(self, actor_id, description, result, title):
        super().__init__()
        self._actor_id = actor_id
        self._description = description
        self._result = result
        self._title = title
        self._units_of_work_ids = []

    def add_unit_of_work(self, uow_id):
        if uow_id in self._units_of_work_ids:
            return Exception(f"Unit of work with id {uow_id} is already part of this project (title: {self._title}, id: {self._id}).")

        self._units_of_work_ids.append(uow_id)

    def remove_unit_of_work(self, uow_id):
        if not uow_id in self._units_of_work_ids:
            return Exception(f"Unit of work with id {uow_id} can't be removed, it is not part of project (title: {self._title}, id: {self._id}).")

        self._units_of_work_ids.remove(uow_id)
