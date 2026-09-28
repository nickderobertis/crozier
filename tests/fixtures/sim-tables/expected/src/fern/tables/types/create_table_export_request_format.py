

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateTableExportRequestFormat(enum.StrEnum):
    """
    Export file format.
    """

    CSV = "csv"
    JSON = "json"

    def visit(self, csv: typing.Callable[[], T_Result], json: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateTableExportRequestFormat.CSV:
            return csv()
        if self is CreateTableExportRequestFormat.JSON:
            return json()
