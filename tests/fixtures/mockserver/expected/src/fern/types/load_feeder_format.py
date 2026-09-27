

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LoadFeederFormat(enum.StrEnum):
    """
    the format of data (required when data is set)
    """

    CSV = "CSV"
    JSON = "JSON"

    def visit(self, csv: typing.Callable[[], T_Result], json: typing.Callable[[], T_Result]) -> T_Result:
        if self is LoadFeederFormat.CSV:
            return csv()
        if self is LoadFeederFormat.JSON:
            return json()
