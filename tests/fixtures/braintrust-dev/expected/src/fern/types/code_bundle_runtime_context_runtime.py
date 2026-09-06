

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CodeBundleRuntimeContextRuntime(enum.StrEnum):
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
        if self is CodeBundleRuntimeContextRuntime.NODE:
            return node()
        if self is CodeBundleRuntimeContextRuntime.PYTHON:
            return python()
        if self is CodeBundleRuntimeContextRuntime.BROWSER:
            return browser()
        if self is CodeBundleRuntimeContextRuntime.QUICKJS:
            return quickjs()
