

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateRequestFormat(enum.StrEnum):
    JSON = "JSON"
    XML = "XML"

    def visit(self, json: typing.Callable[[], T_Result], xml: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateRequestFormat.JSON:
            return json()
        if self is CreateRequestFormat.XML:
            return xml()
