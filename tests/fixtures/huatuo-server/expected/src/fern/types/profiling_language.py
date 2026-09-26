

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProfilingLanguage(enum.StrEnum):
    C = "c"
    CPP = "c++"
    GO = "go"
    JAVA = "java"
    PYTHON = "python"

    def visit(
        self,
        c: typing.Callable[[], T_Result],
        cpp: typing.Callable[[], T_Result],
        go: typing.Callable[[], T_Result],
        java: typing.Callable[[], T_Result],
        python: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProfilingLanguage.C:
            return c()
        if self is ProfilingLanguage.CPP:
            return cpp()
        if self is ProfilingLanguage.GO:
            return go()
        if self is ProfilingLanguage.JAVA:
            return java()
        if self is ProfilingLanguage.PYTHON:
            return python()
