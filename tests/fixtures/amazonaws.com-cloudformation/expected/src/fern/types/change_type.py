

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChangeType(enum.StrEnum):
    """
    The type of entity that CloudFormation changes. Currently, the only entity type is <code>Resource</code>.
    """

    RESOURCE = "Resource"

    def visit(self, resource: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChangeType.RESOURCE:
            return resource()
