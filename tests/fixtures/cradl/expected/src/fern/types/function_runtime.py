

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FunctionRuntime(enum.StrEnum):
    PYTHON = "python"
    NODEJS = "nodejs"

    def visit(self, python: typing.Callable[[], T_Result], nodejs: typing.Callable[[], T_Result]) -> T_Result:
        if self is FunctionRuntime.PYTHON:
            return python()
        if self is FunctionRuntime.NODEJS:
            return nodejs()
