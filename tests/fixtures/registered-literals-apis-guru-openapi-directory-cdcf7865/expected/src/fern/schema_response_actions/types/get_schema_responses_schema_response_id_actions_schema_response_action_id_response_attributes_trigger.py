

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseAttributesTrigger(enum.StrEnum):
    """
    The name of the trigger that caused the action.
    """

    SUBMIT = "submit"
    APPROVE = "approve"
    ACCEPT = "accept"
    ADMIN_REJECT = "admin_reject"
    MODERATOR_REJECT = "moderator_reject"

    def visit(
        self,
        submit: typing.Callable[[], T_Result],
        approve: typing.Callable[[], T_Result],
        accept: typing.Callable[[], T_Result],
        admin_reject: typing.Callable[[], T_Result],
        moderator_reject: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseAttributesTrigger.SUBMIT:
            return submit()
        if self is GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseAttributesTrigger.APPROVE:
            return approve()
        if self is GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseAttributesTrigger.ACCEPT:
            return accept()
        if (
            self
            is GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseAttributesTrigger.ADMIN_REJECT
        ):
            return admin_reject()
        if (
            self
            is GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponseAttributesTrigger.MODERATOR_REJECT
        ):
            return moderator_reject()
