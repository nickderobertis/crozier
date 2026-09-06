

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ForbiddenErrorBodyType(enum.StrEnum):
    ACCESS_DENIED = "accessDenied"

    def visit(self, access_denied: typing.Callable[[], T_Result]) -> T_Result:
        if self is ForbiddenErrorBodyType.ACCESS_DENIED:
            return access_denied()
