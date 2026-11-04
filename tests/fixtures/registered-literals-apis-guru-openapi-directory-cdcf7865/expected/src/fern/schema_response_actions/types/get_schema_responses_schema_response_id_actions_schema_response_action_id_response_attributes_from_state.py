

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseAttributesFromState(enum.StrEnum):
    """
    The name of the state of the Schema Response prior to the creation of the action.
    """

    INITIAL = "initial"
    IN_PROGRESS = "in_progress"
    APPROVED = "approved"
    PENDING_MODERATION = "pending_moderation"

    def visit(
        self,
        initial: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        approved: typing.Callable[[], T_Result],
        pending_moderation: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseAttributesFromState.INITIAL:
            return initial()
        if (
            self
            is GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseAttributesFromState.IN_PROGRESS
        ):
            return in_progress()
        if self is GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseAttributesFromState.APPROVED:
            return approved()
        if (
            self
            is GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseAttributesFromState.PENDING_MODERATION
        ):
            return pending_moderation()
