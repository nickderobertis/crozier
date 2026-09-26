

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanArtifactsItemLifecycleInstallItemGithubReleaseInstallAssetExtractedPathFormat(
    enum.StrEnum
):
    TAR_GZ = "tar.gz"

    def visit(self, tar_gz: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanArtifactsItemLifecycleInstallItemGithubReleaseInstallAssetExtractedPathFormat.TAR_GZ
        ):
            return tar_gz()
