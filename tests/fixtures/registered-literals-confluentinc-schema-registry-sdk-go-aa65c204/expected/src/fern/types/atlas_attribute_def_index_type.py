

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AtlasAttributeDefIndexType(enum.StrEnum):
    DEFAULT = "DEFAULT"
    STRING = "STRING"

    def visit(self, default: typing.Callable[[], T_Result], string: typing.Callable[[], T_Result]) -> T_Result:
        if self is AtlasAttributeDefIndexType.DEFAULT:
            return default()
        if self is AtlasAttributeDefIndexType.STRING:
            return string()
