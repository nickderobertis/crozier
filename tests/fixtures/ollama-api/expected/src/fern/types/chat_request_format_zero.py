

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChatRequestFormatZero(enum.StrEnum):
    JSON = "json"

    def visit(self, json: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChatRequestFormatZero.JSON:
            return json()
