

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsExportAppearance400ResponseName(enum.StrEnum):
    ENGINE_ERROR = "EngineError"

    def visit(self, engine_error: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocAnnotationsExportAppearance400ResponseName.ENGINE_ERROR:
            return engine_error()
