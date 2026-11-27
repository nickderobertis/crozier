

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListProjectCollaborationsRequestRole(enum.StrEnum):
    ADMIN = "ADMIN"
    MEMBER = "MEMBER"

    def visit(self, admin: typing.Callable[[], T_Result], member: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListProjectCollaborationsRequestRole.ADMIN:
            return admin()
        if self is ListProjectCollaborationsRequestRole.MEMBER:
            return member()
