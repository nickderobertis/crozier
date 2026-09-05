

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FunctionDataEndpointType(enum.StrEnum):
    REMOTE_EVAL = "remote_eval"

    def visit(self, remote_eval: typing.Callable[[], T_Result]) -> T_Result:
        if self is FunctionDataEndpointType.REMOTE_EVAL:
            return remote_eval()
