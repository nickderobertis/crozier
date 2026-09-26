

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasureRlSlopeItemFraction(enum.StrEnum):
    DECIMAL = "decimal"
    FRACTION = "fraction"
    ROUND = "round"
    TRUNCATE = "truncate"

    def visit(
        self,
        decimal: typing.Callable[[], T_Result],
        fraction: typing.Callable[[], T_Result],
        round: typing.Callable[[], T_Result],
        truncate: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasureRlSlopeItemFraction.DECIMAL:
            return decimal()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasureRlSlopeItemFraction.FRACTION:
            return fraction()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasureRlSlopeItemFraction.ROUND:
            return round()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasureRlSlopeItemFraction.TRUNCATE:
            return truncate()
