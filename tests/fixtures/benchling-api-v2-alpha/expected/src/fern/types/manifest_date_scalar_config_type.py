

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ManifestDateScalarConfigType(enum.StrEnum):
    DATE = "date"

    def visit(self, date: typing.Callable[[], T_Result]) -> T_Result:
        if self is ManifestDateScalarConfigType.DATE:
            return date()
