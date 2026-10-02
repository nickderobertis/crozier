

import typing

ExpectationCrossProtocolScenariosItemTrigger = typing.Union[
    typing.Literal["DNS_QUERY", "WEBSOCKET_CONNECT", "GRPC_REQUEST", "HTTP_REQUEST"], typing.Any
]
