

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class MappingJobOptionType(str, enum.Enum):
    PUT = "Put"
    CALL = "Call"

    def visit(self, put: typing.Callable[[], T_Result], call: typing.Callable[[], T_Result]) -> T_Result:
        if self is MappingJobOptionType.PUT:
            return put()
        if self is MappingJobOptionType.CALL:
            return call()
