

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ManifestBooleanScalarConfigType(enum.StrEnum):
    BOOLEAN = "boolean"

    def visit(self, boolean: typing.Callable[[], T_Result]) -> T_Result:
        if self is ManifestBooleanScalarConfigType.BOOLEAN:
            return boolean()
