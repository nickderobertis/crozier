

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class RoleType(str, enum.Enum):
    """ """

    READ_ONLY = "READ_ONLY"
    DEVELOPER = "DEVELOPER"
    ADMIN = "ADMIN"

    def visit(
        self,
        read_only: typing.Callable[[], T_Result],
        developer: typing.Callable[[], T_Result],
        admin: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RoleType.READ_ONLY:
            return read_only()
        if self is RoleType.DEVELOPER:
            return developer()
        if self is RoleType.ADMIN:
            return admin()
