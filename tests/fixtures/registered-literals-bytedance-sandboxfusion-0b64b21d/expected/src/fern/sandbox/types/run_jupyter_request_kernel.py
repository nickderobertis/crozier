

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class RunJupyterRequestKernel(enum.StrEnum):
    PYTHON3 = "python3"

    def visit(self, python3: typing.Callable[[], T_Result]) -> T_Result:
        if self is RunJupyterRequestKernel.PYTHON3:
            return python3()
