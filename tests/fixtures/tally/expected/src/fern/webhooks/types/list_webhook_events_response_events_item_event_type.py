

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListWebhookEventsResponseEventsItemEventType(enum.StrEnum):
    """
    Type of event
    """

    FORM_RESPONSE = "FORM_RESPONSE"

    def visit(self, form_response: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListWebhookEventsResponseEventsItemEventType.FORM_RESPONSE:
            return form_response()
