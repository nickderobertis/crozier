

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Role(enum.StrEnum):
    OWNER = "owner"
    DEVELOPER = "developer"
    VIEWER = "viewer"
    SUPPORT = "support"

    def visit(
        self,
        owner: typing.Callable[[], T_Result],
        developer: typing.Callable[[], T_Result],
        viewer: typing.Callable[[], T_Result],
        support: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Role.OWNER:
            return owner()
        if self is Role.DEVELOPER:
            return developer()
        if self is Role.VIEWER:
            return viewer()
        if self is Role.SUPPORT:
            return support()
