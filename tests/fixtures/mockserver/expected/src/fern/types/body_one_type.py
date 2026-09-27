

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BodyOneType(enum.StrEnum):
    JSON = "JSON"

    def visit(self, json: typing.Callable[[], T_Result]) -> T_Result:
        if self is BodyOneType.JSON:
            return json()
