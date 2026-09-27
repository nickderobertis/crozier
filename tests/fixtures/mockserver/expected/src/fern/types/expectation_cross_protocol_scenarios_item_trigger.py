

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExpectationCrossProtocolScenariosItemTrigger(enum.StrEnum):
    DNS_QUERY = "DNS_QUERY"
    WEBSOCKET_CONNECT = "WEBSOCKET_CONNECT"
    GRPC_REQUEST = "GRPC_REQUEST"
    HTTP_REQUEST = "HTTP_REQUEST"

    def visit(
        self,
        dns_query: typing.Callable[[], T_Result],
        websocket_connect: typing.Callable[[], T_Result],
        grpc_request: typing.Callable[[], T_Result],
        http_request: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ExpectationCrossProtocolScenariosItemTrigger.DNS_QUERY:
            return dns_query()
        if self is ExpectationCrossProtocolScenariosItemTrigger.WEBSOCKET_CONNECT:
            return websocket_connect()
        if self is ExpectationCrossProtocolScenariosItemTrigger.GRPC_REQUEST:
            return grpc_request()
        if self is ExpectationCrossProtocolScenariosItemTrigger.HTTP_REQUEST:
            return http_request()
