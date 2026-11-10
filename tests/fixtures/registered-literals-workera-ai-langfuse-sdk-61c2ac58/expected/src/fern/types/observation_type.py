

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObservationType(enum.StrEnum):
    SPAN = "SPAN"
    GENERATION = "GENERATION"
    EVENT = "EVENT"

    def visit(
        self,
        span: typing.Callable[[], T_Result],
        generation: typing.Callable[[], T_Result],
        event: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObservationType.SPAN:
            return span()
        if self is ObservationType.GENERATION:
            return generation()
        if self is ObservationType.EVENT:
            return event()
