

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StartDebTestExecutionRequestExecutionStageOne(enum.StrEnum):
    EMPTY = ""

    def visit(self, empty: typing.Callable[[], T_Result]) -> T_Result:
        if self is StartDebTestExecutionRequestExecutionStageOne.EMPTY:
            return empty()
