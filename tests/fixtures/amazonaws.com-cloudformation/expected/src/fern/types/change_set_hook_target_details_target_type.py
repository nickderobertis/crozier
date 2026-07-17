

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChangeSetHookTargetDetailsTargetType(enum.StrEnum):
    """
    The name of the type.
    """

    RESOURCE = "RESOURCE"

    def visit(self, resource: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChangeSetHookTargetDetailsTargetType.RESOURCE:
            return resource()
