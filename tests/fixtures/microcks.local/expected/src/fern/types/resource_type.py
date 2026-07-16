

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ResourceType(str, enum.Enum):
    """
    Types of managed resources for Services or APIs
    """

    WSDL = "WSDL"
    XSD = "XSD"
    JSON_SCHEMA = "JSON_SCHEMA"
    OPEN_API_SPEC = "OPEN_API_SPEC"
    OPEN_API_SCHEMA = "OPEN_API_SCHEMA"
    ASYNC_API_SPEC = "ASYNC_API_SPEC"
    ASYNC_API_SCHEMA = "ASYNC_API_SCHEMA"
    AVRO_SCHEMA = "AVRO_SCHEMA"
    PROTOBUF_SCHEMA = "PROTOBUF_SCHEMA"
    PROTOBUF_DESCRIPTION = "PROTOBUF_DESCRIPTION"
    GRAPHQL_SCHEMA = "GRAPHQL_SCHEMA"

    def visit(
        self,
        wsdl: typing.Callable[[], T_Result],
        xsd: typing.Callable[[], T_Result],
        json_schema: typing.Callable[[], T_Result],
        open_api_spec: typing.Callable[[], T_Result],
        open_api_schema: typing.Callable[[], T_Result],
        async_api_spec: typing.Callable[[], T_Result],
        async_api_schema: typing.Callable[[], T_Result],
        avro_schema: typing.Callable[[], T_Result],
        protobuf_schema: typing.Callable[[], T_Result],
        protobuf_description: typing.Callable[[], T_Result],
        graphql_schema: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ResourceType.WSDL:
            return wsdl()
        if self is ResourceType.XSD:
            return xsd()
        if self is ResourceType.JSON_SCHEMA:
            return json_schema()
        if self is ResourceType.OPEN_API_SPEC:
            return open_api_spec()
        if self is ResourceType.OPEN_API_SCHEMA:
            return open_api_schema()
        if self is ResourceType.ASYNC_API_SPEC:
            return async_api_spec()
        if self is ResourceType.ASYNC_API_SCHEMA:
            return async_api_schema()
        if self is ResourceType.AVRO_SCHEMA:
            return avro_schema()
        if self is ResourceType.PROTOBUF_SCHEMA:
            return protobuf_schema()
        if self is ResourceType.PROTOBUF_DESCRIPTION:
            return protobuf_description()
        if self is ResourceType.GRAPHQL_SCHEMA:
            return graphql_schema()
