

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EvalResultOutputExtractedType(enum.StrEnum):
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
        if self is EvalResultOutputExtractedType.FENCED:
            return fenced()
        if self is EvalResultOutputExtractedType.INCOMPLETE_FENCED:
            return incomplete_fenced()
        if self is EvalResultOutputExtractedType.HEURISTIC:
            return heuristic()
        if self is EvalResultOutputExtractedType.EMPTY:
            return empty()
