

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResponseFormatNullishJsonSchemaType(enum.StrEnum):
    JSON_SCHEMA = "json_schema"

    def visit(self, json_schema: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResponseFormatNullishJsonSchemaType.JSON_SCHEMA:
            return json_schema()
