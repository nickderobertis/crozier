

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NotificationCategory(enum.StrEnum):
    NEW_ORGANIZATION = "NEW_ORGANIZATION"
    STUDY_SHARED = "STUDY_SHARED"
    TEMPLATE_SHARED = "TEMPLATE_SHARED"
    CONVERSATION_NOTIFICATION = "CONVERSATION_NOTIFICATION"
    ANNOTATION_NOTE = "ANNOTATION_NOTE"
    WALLET_SHARED = "WALLET_SHARED"

    def visit(
        self,
        new_organization: typing.Callable[[], T_Result],
        study_shared: typing.Callable[[], T_Result],
        template_shared: typing.Callable[[], T_Result],
        conversation_notification: typing.Callable[[], T_Result],
        annotation_note: typing.Callable[[], T_Result],
        wallet_shared: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is NotificationCategory.NEW_ORGANIZATION:
            return new_organization()
        if self is NotificationCategory.STUDY_SHARED:
            return study_shared()
        if self is NotificationCategory.TEMPLATE_SHARED:
            return template_shared()
        if self is NotificationCategory.CONVERSATION_NOTIFICATION:
            return conversation_notification()
        if self is NotificationCategory.ANNOTATION_NOTE:
            return annotation_note()
        if self is NotificationCategory.WALLET_SHARED:
            return wallet_shared()
