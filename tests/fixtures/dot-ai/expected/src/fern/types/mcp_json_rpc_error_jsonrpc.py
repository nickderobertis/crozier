

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class McpJsonRpcErrorJsonrpc(enum.StrEnum):
    """
    JSON-RPC version
    """

    TWO0 = "2.0"

    def visit(self, two0: typing.Callable[[], T_Result]) -> T_Result:
        if self is McpJsonRpcErrorJsonrpc.TWO0:
            return two0()
