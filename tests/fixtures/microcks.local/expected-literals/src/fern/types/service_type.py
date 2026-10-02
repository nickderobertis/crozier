

import typing

ServiceType = typing.Union[
    typing.Literal["REST", "SOAP_HTTP", "GENERIC_REST", "GENERIC_EVENT", "EVENT", "GRPC", "GRAPHQL"], typing.Any
]
