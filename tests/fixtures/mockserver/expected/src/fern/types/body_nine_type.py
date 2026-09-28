

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BodyNineType(enum.StrEnum):
    XML = "XML"

    def visit(self, xml: typing.Callable[[], T_Result]) -> T_Result:
        if self is BodyNineType.XML:
            return xml()
