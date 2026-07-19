

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IdentityType(enum.StrEnum):
    """
    Enum to represent the type of the identity.
    """

    ORG = "org"
    USER = "user"
    OTHER = "other"

    def visit(
        self,
        org: typing.Callable[[], T_Result],
        user: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IdentityType.ORG:
            return org()
        if self is IdentityType.USER:
            return user()
        if self is IdentityType.OTHER:
            return other()
