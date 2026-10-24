

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Role(enum.StrEnum):
    VIEWER = "viewer"
    OPERATOR = "operator"
    ADMIN = "admin"
    OWNER = "owner"

    def visit(
        self,
        viewer: typing.Callable[[], T_Result],
        operator: typing.Callable[[], T_Result],
        admin: typing.Callable[[], T_Result],
        owner: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Role.VIEWER:
            return viewer()
        if self is Role.OPERATOR:
            return operator()
        if self is Role.ADMIN:
            return admin()
        if self is Role.OWNER:
            return owner()
