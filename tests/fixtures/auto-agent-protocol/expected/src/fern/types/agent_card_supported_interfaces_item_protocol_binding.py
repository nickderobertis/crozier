

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AgentCardSupportedInterfacesItemProtocolBinding(enum.StrEnum):
    """
    The A2A transport binding available at this URL.
    """

    JSONRPC = "JSONRPC"
    HTTP_JSON = "HTTP+JSON"

    def visit(self, jsonrpc: typing.Callable[[], T_Result], http_json: typing.Callable[[], T_Result]) -> T_Result:
        if self is AgentCardSupportedInterfacesItemProtocolBinding.JSONRPC:
            return jsonrpc()
        if self is AgentCardSupportedInterfacesItemProtocolBinding.HTTP_JSON:
            return http_json()
