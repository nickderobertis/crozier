

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanArtifactsItemLifecycleInstallItemGithubReleaseInstallReleaseKindKind(
    enum.StrEnum
):
    TAG = "tag"

    def visit(self, tag: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanArtifactsItemLifecycleInstallItemGithubReleaseInstallReleaseKindKind.TAG
        ):
            return tag()
