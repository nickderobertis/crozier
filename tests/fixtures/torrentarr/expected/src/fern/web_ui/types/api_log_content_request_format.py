

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ApiLogContentRequestFormat(enum.StrEnum):
    JSON = "json"

    def visit(self, json: typing.Callable[[], T_Result]) -> T_Result:
        if self is ApiLogContentRequestFormat.JSON:
            return json()
