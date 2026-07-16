

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetActivateTypeRequestAction(enum.StrEnum):
    ACTIVATE_TYPE = "ActivateType"

    def visit(self, activate_type: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetActivateTypeRequestAction.ACTIVATE_TYPE:
            return activate_type()
