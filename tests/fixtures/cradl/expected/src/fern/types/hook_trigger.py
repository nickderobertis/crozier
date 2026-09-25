

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HookTrigger(enum.StrEnum):
    ACTION_RUN_HAS_COMPLETED = "ActionRun has Completed"
    DOCUMENT_IS_CREATED = "Document is Created"
    EMAIL_IS_RECEIVED = "Email is Received"
    PREDICTION_IS_CREATED = "Prediction is Created"
    VALIDATION_TASK_HAS_COMPLETED = "ValidationTask has Completed"
    VALIDATION_TASK_IS_CREATED = "ValidationTask is Created"

    def visit(
        self,
        action_run_has_completed: typing.Callable[[], T_Result],
        document_is_created: typing.Callable[[], T_Result],
        email_is_received: typing.Callable[[], T_Result],
        prediction_is_created: typing.Callable[[], T_Result],
        validation_task_has_completed: typing.Callable[[], T_Result],
        validation_task_is_created: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is HookTrigger.ACTION_RUN_HAS_COMPLETED:
            return action_run_has_completed()
        if self is HookTrigger.DOCUMENT_IS_CREATED:
            return document_is_created()
        if self is HookTrigger.EMAIL_IS_RECEIVED:
            return email_is_received()
        if self is HookTrigger.PREDICTION_IS_CREATED:
            return prediction_is_created()
        if self is HookTrigger.VALIDATION_TASK_HAS_COMPLETED:
            return validation_task_has_completed()
        if self is HookTrigger.VALIDATION_TASK_IS_CREATED:
            return validation_task_is_created()
