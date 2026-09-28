

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BodyMethodType(enum.StrEnum):
    JSON_RPC = "JSON_RPC"

    def visit(self, json_rpc: typing.Callable[[], T_Result]) -> T_Result:
        if self is BodyMethodType.JSON_RPC:
            return json_rpc()
