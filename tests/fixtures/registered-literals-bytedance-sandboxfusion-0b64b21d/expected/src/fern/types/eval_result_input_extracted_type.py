

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EvalResultInputExtractedType(enum.StrEnum):
    FENCED = "fenced"
    INCOMPLETE_FENCED = "incomplete_fenced"
    HEURISTIC = "heuristic"
    EMPTY = "empty"

    def visit(
        self,
        fenced: typing.Callable[[], T_Result],
        incomplete_fenced: typing.Callable[[], T_Result],
        heuristic: typing.Callable[[], T_Result],
        empty: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EvalResultInputExtractedType.FENCED:
            return fenced()
        if self is EvalResultInputExtractedType.INCOMPLETE_FENCED:
            return incomplete_fenced()
        if self is EvalResultInputExtractedType.HEURISTIC:
            return heuristic()
        if self is EvalResultInputExtractedType.EMPTY:
            return empty()
