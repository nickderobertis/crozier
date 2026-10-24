

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransportType(enum.StrEnum):
    JSON_RPC = "JsonRpc"

    def visit(self, json_rpc: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransportType.JSON_RPC:
            return json_rpc()
