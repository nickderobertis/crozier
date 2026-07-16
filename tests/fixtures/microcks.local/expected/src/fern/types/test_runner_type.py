

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TestRunnerType(enum.StrEnum):
    """
    Type of test strategy (different strategies are implemented by different runners)
    """

    HTTP = "HTTP"
    SOAP_HTTP = "SOAP_HTTP"
    SOAP_UI = "SOAP_UI"
    POSTMAN = "POSTMAN"
    OPEN_API_SCHEMA = "OPEN_API_SCHEMA"
    ASYNC_API_SCHEMA = "ASYNC_API_SCHEMA"
    GRPC_PROTOBUF = "GRPC_PROTOBUF"
    GRAPHQL_SCHEMA = "GRAPHQL_SCHEMA"

    def visit(
        self,
        http: typing.Callable[[], T_Result],
        soap_http: typing.Callable[[], T_Result],
        soap_ui: typing.Callable[[], T_Result],
        postman: typing.Callable[[], T_Result],
        open_api_schema: typing.Callable[[], T_Result],
        async_api_schema: typing.Callable[[], T_Result],
        grpc_protobuf: typing.Callable[[], T_Result],
        graphql_schema: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TestRunnerType.HTTP:
            return http()
        if self is TestRunnerType.SOAP_HTTP:
            return soap_http()
        if self is TestRunnerType.SOAP_UI:
            return soap_ui()
        if self is TestRunnerType.POSTMAN:
            return postman()
        if self is TestRunnerType.OPEN_API_SCHEMA:
            return open_api_schema()
        if self is TestRunnerType.ASYNC_API_SCHEMA:
            return async_api_schema()
        if self is TestRunnerType.GRPC_PROTOBUF:
            return grpc_protobuf()
        if self is TestRunnerType.GRAPHQL_SCHEMA:
            return graphql_schema()
