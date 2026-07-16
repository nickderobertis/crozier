

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetDeactivateTypeRequestAction(str, enum.Enum):
    DEACTIVATE_TYPE = "DeactivateType"

    def visit(self, deactivate_type: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetDeactivateTypeRequestAction.DEACTIVATE_TYPE:
            return deactivate_type()
