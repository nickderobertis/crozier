

import typing

ResourceType = typing.Union[
    typing.Literal[
        "WSDL",
        "XSD",
        "JSON_SCHEMA",
        "OPEN_API_SPEC",
        "OPEN_API_SCHEMA",
        "ASYNC_API_SPEC",
        "ASYNC_API_SCHEMA",
        "AVRO_SCHEMA",
        "PROTOBUF_SCHEMA",
        "PROTOBUF_DESCRIPTION",
        "GRAPHQL_SCHEMA",
    ],
    typing.Any,
]
