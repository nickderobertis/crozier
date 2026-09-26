

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemEndpointsItemConnectionMode(
    enum.StrEnum
):
    DEDICATED = "dedicated"
    SHARED = "shared"

    def visit(self, dedicated: typing.Callable[[], T_Result], shared: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemEndpointsItemConnectionMode.DEDICATED
        ):
            return dedicated()
        if (
            self
            is PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemEndpointsItemConnectionMode.SHARED
        ):
            return shared()
