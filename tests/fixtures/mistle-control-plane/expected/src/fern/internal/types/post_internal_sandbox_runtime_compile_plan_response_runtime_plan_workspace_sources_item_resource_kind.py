

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanWorkspaceSourcesItemResourceKind(enum.StrEnum):
    REPOSITORY = "repository"

    def visit(self, repository: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanWorkspaceSourcesItemResourceKind.REPOSITORY:
            return repository()
