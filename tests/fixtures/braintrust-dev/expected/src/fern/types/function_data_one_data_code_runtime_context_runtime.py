

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FunctionDataOneDataCodeRuntimeContextRuntime(enum.StrEnum):
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
        if self is FunctionDataOneDataCodeRuntimeContextRuntime.NODE:
            return node()
        if self is FunctionDataOneDataCodeRuntimeContextRuntime.PYTHON:
            return python()
        if self is FunctionDataOneDataCodeRuntimeContextRuntime.BROWSER:
            return browser()
        if self is FunctionDataOneDataCodeRuntimeContextRuntime.QUICKJS:
            return quickjs()
