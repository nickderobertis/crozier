

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ManifestFloatScalarConfigType(enum.StrEnum):
    FLOAT = "float"

    def visit(self, float_: typing.Callable[[], T_Result]) -> T_Result:
        if self is ManifestFloatScalarConfigType.FLOAT:
            return float_()
