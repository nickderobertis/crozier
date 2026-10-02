

import typing

TestRunnerType = typing.Union[
    typing.Literal[
        "HTTP",
        "SOAP_HTTP",
        "SOAP_UI",
        "POSTMAN",
        "OPEN_API_SCHEMA",
        "ASYNC_API_SCHEMA",
        "GRPC_PROTOBUF",
        "GRAPHQL_SCHEMA",
    ],
    typing.Any,
]
