

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteRequestTransport(enum.StrEnum):
    HTTP = "http"
    WEBSOCKET = "websocket"

    def visit(self, http: typing.Callable[[], T_Result], websocket: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteRequestTransport.HTTP:
            return http()
        if self is PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteRequestTransport.WEBSOCKET:
            return websocket()
