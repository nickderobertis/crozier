

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationTargetRolesItemSeventeen(enum.StrEnum):
    ACCESSORY = "accessory"

    def visit(self, accessory: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationTargetRolesItemSeventeen.ACCESSORY:
            return accessory()
