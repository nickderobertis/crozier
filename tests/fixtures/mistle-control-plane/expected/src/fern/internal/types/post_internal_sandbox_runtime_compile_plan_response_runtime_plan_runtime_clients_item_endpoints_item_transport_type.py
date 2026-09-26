

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemEndpointsItemTransportType(
    enum.StrEnum
):
    WS = "ws"

    def visit(self, ws: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemEndpointsItemTransportType.WS
        ):
            return ws()
