

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResponseFormatNullishZeroType(enum.StrEnum):
    JSON_OBJECT = "json_object"

    def visit(self, json_object: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResponseFormatNullishZeroType.JSON_OBJECT:
            return json_object()
