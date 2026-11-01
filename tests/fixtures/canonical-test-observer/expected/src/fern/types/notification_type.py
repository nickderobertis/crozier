

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NotificationType(enum.StrEnum):
    USER_ASSIGNED_ARTEFACT_REVIEW = "USER_ASSIGNED_ARTEFACT_REVIEW"
    USER_ASSIGNED_ENVIRONMENT_REVIEW = "USER_ASSIGNED_ENVIRONMENT_REVIEW"

    def visit(
        self,
        user_assigned_artefact_review: typing.Callable[[], T_Result],
        user_assigned_environment_review: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is NotificationType.USER_ASSIGNED_ARTEFACT_REVIEW:
            return user_assigned_artefact_review()
        if self is NotificationType.USER_ASSIGNED_ENVIRONMENT_REVIEW:
            return user_assigned_environment_review()
