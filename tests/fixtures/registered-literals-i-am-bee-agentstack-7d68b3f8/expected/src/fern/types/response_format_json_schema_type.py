

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResponseFormatJsonSchemaType(enum.StrEnum):
    JSON_SCHEMA = "json_schema"

    def visit(self, json_schema: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResponseFormatJsonSchemaType.JSON_SCHEMA:
            return json_schema()
