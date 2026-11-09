

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetScoresResponseDataTwoDataType(enum.StrEnum):
    BOOLEAN = "BOOLEAN"

    def visit(self, boolean: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetScoresResponseDataTwoDataType.BOOLEAN:
            return boolean()
