

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ManifestIntegerScalarConfigType(enum.StrEnum):
    INTEGER = "integer"

    def visit(self, integer: typing.Callable[[], T_Result]) -> T_Result:
        if self is ManifestIntegerScalarConfigType.INTEGER:
            return integer()
