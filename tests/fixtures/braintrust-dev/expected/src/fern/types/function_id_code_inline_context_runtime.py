

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FunctionIdCodeInlineContextRuntime(enum.StrEnum):
    NODE = "node"
    PYTHON = "python"
    BROWSER = "browser"
    QUICKJS = "quickjs"

    def visit(
        self,
        node: typing.Callable[[], T_Result],
        python: typing.Callable[[], T_Result],
        browser: typing.Callable[[], T_Result],
        quickjs: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FunctionIdCodeInlineContextRuntime.NODE:
            return node()
        if self is FunctionIdCodeInlineContextRuntime.PYTHON:
            return python()
        if self is FunctionIdCodeInlineContextRuntime.BROWSER:
            return browser()
        if self is FunctionIdCodeInlineContextRuntime.QUICKJS:
            return quickjs()
