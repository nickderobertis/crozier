

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ManifestDatetimeScalarConfigType(enum.StrEnum):
    DATETIME = "datetime"

    def visit(self, datetime: typing.Callable[[], T_Result]) -> T_Result:
        if self is ManifestDatetimeScalarConfigType.DATETIME:
            return datetime()
