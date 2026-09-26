

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanArtifactsItemLifecycleInstallItemGithubReleaseInstallAssetZeroFormat(
    enum.StrEnum
):
    BINARY = "binary"

    def visit(self, binary: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanArtifactsItemLifecycleInstallItemGithubReleaseInstallAssetZeroFormat.BINARY
        ):
            return binary()
