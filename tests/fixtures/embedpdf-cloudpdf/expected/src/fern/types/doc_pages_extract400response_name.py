

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocPagesExtract400ResponseName(enum.StrEnum):
    ENGINE_ERROR = "EngineError"

    def visit(self, engine_error: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocPagesExtract400ResponseName.ENGINE_ERROR:
            return engine_error()
