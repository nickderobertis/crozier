

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ChangeSetHookTargetDetailsTargetType(str, enum.Enum):
    """
    The name of the type.
    """

    RESOURCE = "RESOURCE"

    def visit(self, resource: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChangeSetHookTargetDetailsTargetType.RESOURCE:
            return resource()
