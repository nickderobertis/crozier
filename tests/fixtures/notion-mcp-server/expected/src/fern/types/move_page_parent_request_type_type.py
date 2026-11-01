

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MovePageParentRequestTypeType(enum.StrEnum):
    WORKSPACE = "workspace"

    def visit(self, workspace: typing.Callable[[], T_Result]) -> T_Result:
        if self is MovePageParentRequestTypeType.WORKSPACE:
            return workspace()
