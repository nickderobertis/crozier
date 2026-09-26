

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemSetupFilesItemWriteMode(enum.StrEnum):
    OVERWRITE = "overwrite"
    IF_ABSENT = "if-absent"
    MERGE = "merge"

    def visit(
        self,
        overwrite: typing.Callable[[], T_Result],
        if_absent: typing.Callable[[], T_Result],
        merge: typing.Callable[[], T_Result],
    ) -> T_Result:
        if (
            self
            is PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemSetupFilesItemWriteMode.OVERWRITE
        ):
            return overwrite()
        if (
            self
            is PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemSetupFilesItemWriteMode.IF_ABSENT
        ):
            return if_absent()
        if (
            self
            is PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemSetupFilesItemWriteMode.MERGE
        ):
            return merge()
