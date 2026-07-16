

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ServiceType(str, enum.Enum):
    """
    Service or API Type
    """

    REST = "REST"
    SOAP_HTTP = "SOAP_HTTP"
    GENERIC_REST = "GENERIC_REST"
    GENERIC_EVENT = "GENERIC_EVENT"
    EVENT = "EVENT"
    GRPC = "GRPC"
    GRAPHQL = "GRAPHQL"

    def visit(
        self,
        rest: typing.Callable[[], T_Result],
        soap_http: typing.Callable[[], T_Result],
        generic_rest: typing.Callable[[], T_Result],
        generic_event: typing.Callable[[], T_Result],
        event: typing.Callable[[], T_Result],
        grpc: typing.Callable[[], T_Result],
        graphql: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ServiceType.REST:
            return rest()
        if self is ServiceType.SOAP_HTTP:
            return soap_http()
        if self is ServiceType.GENERIC_REST:
            return generic_rest()
        if self is ServiceType.GENERIC_EVENT:
            return generic_event()
        if self is ServiceType.EVENT:
            return event()
        if self is ServiceType.GRPC:
            return grpc()
        if self is ServiceType.GRAPHQL:
            return graphql()
