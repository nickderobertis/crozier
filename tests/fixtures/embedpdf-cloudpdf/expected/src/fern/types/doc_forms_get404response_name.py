

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocFormsGet404ResponseName(enum.StrEnum):
    ENGINE_ERROR = "EngineError"

    def visit(self, engine_error: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocFormsGet404ResponseName.ENGINE_ERROR:
            return engine_error()
