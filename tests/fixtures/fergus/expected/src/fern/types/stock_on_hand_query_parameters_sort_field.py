

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StockOnHandQueryParametersSortField(enum.StrEnum):
    DATE_ENTERED = "dateEntered"
    LAST_MODIFIED = "lastModified"

    def visit(
        self, date_entered: typing.Callable[[], T_Result], last_modified: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is StockOnHandQueryParametersSortField.DATE_ENTERED:
            return date_entered()
        if self is StockOnHandQueryParametersSortField.LAST_MODIFIED:
            return last_modified()
