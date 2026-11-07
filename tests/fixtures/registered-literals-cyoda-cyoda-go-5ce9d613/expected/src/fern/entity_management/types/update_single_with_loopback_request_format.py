

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateSingleWithLoopbackRequestFormat(enum.StrEnum):
    JSON = "JSON"
    XML = "XML"

    def visit(self, json: typing.Callable[[], T_Result], xml: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdateSingleWithLoopbackRequestFormat.JSON:
            return json()
        if self is UpdateSingleWithLoopbackRequestFormat.XML:
            return xml()
