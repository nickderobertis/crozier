

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MappingJobOptionType(enum.StrEnum):
    PUT = "Put"
    CALL = "Call"

    def visit(self, put: typing.Callable[[], T_Result], call: typing.Callable[[], T_Result]) -> T_Result:
        if self is MappingJobOptionType.PUT:
            return put()
        if self is MappingJobOptionType.CALL:
            return call()
