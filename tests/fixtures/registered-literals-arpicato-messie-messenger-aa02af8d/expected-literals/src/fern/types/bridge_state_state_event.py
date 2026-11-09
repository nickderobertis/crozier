

import typing

BridgeStateStateEvent = typing.Union[
    typing.Literal["CONNECTING", "CONNECTED", "TRANSIENT_DISCONNECT", "BAD_CREDENTIALS", "UNKNOWN_ERROR"], typing.Any
]
