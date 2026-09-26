

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostInternalSandboxRuntimeCompilePlanRequestSnapshotPreparationScriptKind(enum.StrEnum):
    SETUP = "setup"
    MAINTENANCE = "maintenance"

    def visit(self, setup: typing.Callable[[], T_Result], maintenance: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostInternalSandboxRuntimeCompilePlanRequestSnapshotPreparationScriptKind.SETUP:
            return setup()
        if self is PostInternalSandboxRuntimeCompilePlanRequestSnapshotPreparationScriptKind.MAINTENANCE:
            return maintenance()
