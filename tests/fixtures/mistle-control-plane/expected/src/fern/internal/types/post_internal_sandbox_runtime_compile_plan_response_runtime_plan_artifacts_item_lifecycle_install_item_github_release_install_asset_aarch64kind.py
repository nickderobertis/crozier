

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanArtifactsItemLifecycleInstallItemGithubReleaseInstallAssetAarch64Kind(
    enum.StrEnum
):
    BY_ARCH = "by_arch"

    def visit(self, by_arch: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanArtifactsItemLifecycleInstallItemGithubReleaseInstallAssetAarch64Kind.BY_ARCH
        ):
            return by_arch()
