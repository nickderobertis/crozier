

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListTaskSummariesRequestResource(enum.StrEnum):
    USERS = "users"
    PROJECTS = "projects"

    def visit(self, users: typing.Callable[[], T_Result], projects: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListTaskSummariesRequestResource.USERS:
            return users()
        if self is ListTaskSummariesRequestResource.PROJECTS:
            return projects()
