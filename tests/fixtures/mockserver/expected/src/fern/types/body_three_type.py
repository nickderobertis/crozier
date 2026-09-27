

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BodyThreeType(enum.StrEnum):
    JSON_SCHEMA = "JSON_SCHEMA"

    def visit(self, json_schema: typing.Callable[[], T_Result]) -> T_Result:
        if self is BodyThreeType.JSON_SCHEMA:
            return json_schema()
