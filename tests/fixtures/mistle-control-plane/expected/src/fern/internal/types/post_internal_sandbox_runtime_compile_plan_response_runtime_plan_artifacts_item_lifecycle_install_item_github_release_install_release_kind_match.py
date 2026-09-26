

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanArtifactsItemLifecycleInstallItemGithubReleaseInstallReleaseKindMatch(
    enum.StrEnum
):
    LATEST_MATCHING_PREFIX = "latest_matching_prefix"

    def visit(self, latest_matching_prefix: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanArtifactsItemLifecycleInstallItemGithubReleaseInstallReleaseKindMatch.LATEST_MATCHING_PREFIX
        ):
            return latest_matching_prefix()
