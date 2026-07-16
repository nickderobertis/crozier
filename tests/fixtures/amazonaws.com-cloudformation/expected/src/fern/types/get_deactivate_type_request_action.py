

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetDeactivateTypeRequestAction(enum.StrEnum):
    DEACTIVATE_TYPE = "DeactivateType"

    def visit(self, deactivate_type: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetDeactivateTypeRequestAction.DEACTIVATE_TYPE:
            return deactivate_type()
