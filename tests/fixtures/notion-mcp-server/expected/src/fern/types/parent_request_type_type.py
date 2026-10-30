

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ParentRequestTypeType(enum.StrEnum):
    WORKSPACE = "workspace"

    def visit(self, workspace: typing.Callable[[], T_Result]) -> T_Result:
        if self is ParentRequestTypeType.WORKSPACE:
            return workspace()
