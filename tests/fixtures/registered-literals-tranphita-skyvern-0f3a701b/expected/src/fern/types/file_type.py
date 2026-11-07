

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FileType(enum.StrEnum):
    CSV = "csv"

    def visit(self, csv: typing.Callable[[], T_Result]) -> T_Result:
        if self is FileType.CSV:
            return csv()
