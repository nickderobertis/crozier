

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarimoTableGetDataUrlOutputFormat(enum.StrEnum):
    CSV = "csv"
    JSON = "json"
    ARROW = "arrow"

    def visit(
        self,
        csv: typing.Callable[[], T_Result],
        json: typing.Callable[[], T_Result],
        arrow: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MarimoTableGetDataUrlOutputFormat.CSV:
            return csv()
        if self is MarimoTableGetDataUrlOutputFormat.JSON:
            return json()
        if self is MarimoTableGetDataUrlOutputFormat.ARROW:
            return arrow()
