

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostA2ARequestJsonrpc(enum.StrEnum):
    """
    JSON-RPC version
    """

    TWO0 = "2.0"

    def visit(self, two0: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostA2ARequestJsonrpc.TWO0:
            return two0()
