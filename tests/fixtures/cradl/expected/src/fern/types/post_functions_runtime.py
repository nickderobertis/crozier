

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostFunctionsRuntime(enum.StrEnum):
    PYTHON = "python"
    NODEJS = "nodejs"

    def visit(self, python: typing.Callable[[], T_Result], nodejs: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostFunctionsRuntime.PYTHON:
            return python()
        if self is PostFunctionsRuntime.NODEJS:
            return nodejs()
