

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateSingleRequestFormat(enum.StrEnum):
    JSON = "JSON"
    XML = "XML"

    def visit(self, json: typing.Callable[[], T_Result], xml: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdateSingleRequestFormat.JSON:
            return json()
        if self is UpdateSingleRequestFormat.XML:
            return xml()
