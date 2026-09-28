

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BodyFourType(enum.StrEnum):
    JSON_PATH = "JSON_PATH"

    def visit(self, json_path: typing.Callable[[], T_Result]) -> T_Result:
        if self is BodyFourType.JSON_PATH:
            return json_path()
