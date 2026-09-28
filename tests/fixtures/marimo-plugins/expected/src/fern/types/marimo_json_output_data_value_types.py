

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarimoJsonOutputDataValueTypes(enum.StrEnum):
    JSON = "json"
    PYTHON = "python"

    def visit(self, json: typing.Callable[[], T_Result], python: typing.Callable[[], T_Result]) -> T_Result:
        if self is MarimoJsonOutputDataValueTypes.JSON:
            return json()
        if self is MarimoJsonOutputDataValueTypes.PYTHON:
            return python()
