

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanWorkspaceSourcesItemSourceKind(enum.StrEnum):
    GIT_CLONE = "git-clone"

    def visit(self, git_clone: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanWorkspaceSourcesItemSourceKind.GIT_CLONE:
            return git_clone()
