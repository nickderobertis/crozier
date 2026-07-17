

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostActivateTypeRequestAction(enum.StrEnum):
    ACTIVATE_TYPE = "ActivateType"

    def visit(self, activate_type: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostActivateTypeRequestAction.ACTIVATE_TYPE:
            return activate_type()
