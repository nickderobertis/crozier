

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListFolderCollaborationsRequestRole(enum.StrEnum):
    ADMIN = "ADMIN"
    MEMBER = "MEMBER"

    def visit(self, admin: typing.Callable[[], T_Result], member: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListFolderCollaborationsRequestRole.ADMIN:
            return admin()
        if self is ListFolderCollaborationsRequestRole.MEMBER:
            return member()
