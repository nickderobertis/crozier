

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Error401Name(enum.StrEnum):
    AUTHENTICATION_FAILURE = "AUTHENTICATION_FAILURE"

    def visit(self, authentication_failure: typing.Callable[[], T_Result]) -> T_Result:
        if self is Error401Name.AUTHENTICATION_FAILURE:
            return authentication_failure()
