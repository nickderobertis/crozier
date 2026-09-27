

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationTargetRolesItemSixteen(enum.StrEnum):
    CLOTHING = "clothing"

    def visit(self, clothing: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationTargetRolesItemSixteen.CLOTHING:
            return clothing()
