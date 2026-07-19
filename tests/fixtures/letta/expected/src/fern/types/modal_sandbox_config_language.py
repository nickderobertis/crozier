

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModalSandboxConfigLanguage(enum.StrEnum):
    PYTHON = "python"
    TYPESCRIPT = "typescript"

    def visit(self, python: typing.Callable[[], T_Result], typescript: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModalSandboxConfigLanguage.PYTHON:
            return python()
        if self is ModalSandboxConfigLanguage.TYPESCRIPT:
            return typescript()
