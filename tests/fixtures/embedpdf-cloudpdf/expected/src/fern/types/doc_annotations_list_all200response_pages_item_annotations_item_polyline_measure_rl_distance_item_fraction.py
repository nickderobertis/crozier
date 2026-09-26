

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineMeasureRlDistanceItemFraction(enum.StrEnum):
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
        if (
            self
            is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineMeasureRlDistanceItemFraction.DECIMAL
        ):
            return decimal()
        if (
            self
            is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineMeasureRlDistanceItemFraction.FRACTION
        ):
            return fraction()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineMeasureRlDistanceItemFraction.ROUND:
            return round()
        if (
            self
            is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineMeasureRlDistanceItemFraction.TRUNCATE
        ):
            return truncate()
