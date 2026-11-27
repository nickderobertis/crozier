

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ManifestArrayConfigType(enum.StrEnum):
    ARRAY = "array"

    def visit(self, array: typing.Callable[[], T_Result]) -> T_Result:
        if self is ManifestArrayConfigType.ARRAY:
            return array()
