

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FunctionDataNullishEndpointType(enum.StrEnum):
    REMOTE_EVAL = "remote_eval"

    def visit(self, remote_eval: typing.Callable[[], T_Result]) -> T_Result:
        if self is FunctionDataNullishEndpointType.REMOTE_EVAL:
            return remote_eval()
