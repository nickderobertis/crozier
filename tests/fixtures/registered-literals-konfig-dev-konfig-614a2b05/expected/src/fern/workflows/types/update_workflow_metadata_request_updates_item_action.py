

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateWorkflowMetadataRequestUpdatesItemAction(enum.StrEnum):
    """
    The type of action you'd like to take on an existing attribute (read-only fields cannot be updated). Use the remove action to clear values. If using the remove action, the attribute cannot be required by the workflow.
    """

    SET = "set"
    REMOVE = "remove"

    def visit(self, set_: typing.Callable[[], T_Result], remove: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdateWorkflowMetadataRequestUpdatesItemAction.SET:
            return set_()
        if self is UpdateWorkflowMetadataRequestUpdatesItemAction.REMOVE:
            return remove()
