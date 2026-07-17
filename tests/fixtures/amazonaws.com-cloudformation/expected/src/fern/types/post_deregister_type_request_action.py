

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostDeregisterTypeRequestAction(enum.StrEnum):
    DEREGISTER_TYPE = "DeregisterType"

    def visit(self, deregister_type: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostDeregisterTypeRequestAction.DEREGISTER_TYPE:
            return deregister_type()
