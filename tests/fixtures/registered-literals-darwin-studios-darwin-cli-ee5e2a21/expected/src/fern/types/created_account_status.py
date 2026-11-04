

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreatedAccountStatus(enum.StrEnum):
    UNVERIFIED = "unverified"

    def visit(self, unverified: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreatedAccountStatus.UNVERIFIED:
            return unverified()
