

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ScoreTwoDataType(enum.StrEnum):
    BOOLEAN = "BOOLEAN"

    def visit(self, boolean: typing.Callable[[], T_Result]) -> T_Result:
        if self is ScoreTwoDataType.BOOLEAN:
            return boolean()
