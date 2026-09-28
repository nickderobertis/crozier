

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class McpJsonRpcResponseJsonrpc(enum.StrEnum):
    """
    JSON-RPC version
    """

    TWO0 = "2.0"

    def visit(self, two0: typing.Callable[[], T_Result]) -> T_Result:
        if self is McpJsonRpcResponseJsonrpc.TWO0:
            return two0()
