

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LinkDeliveryWebhookCallbackType(enum.StrEnum):
    """
    The type of Link callback event
    """

    ON_SUCCESS = "ON_SUCCESS"
    ON_EVENT = "ON_EVENT"
    ON_EXIT = "ON_EXIT"

    def visit(
        self,
        on_success: typing.Callable[[], T_Result],
        on_event: typing.Callable[[], T_Result],
        on_exit: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LinkDeliveryWebhookCallbackType.ON_SUCCESS:
            return on_success()
        if self is LinkDeliveryWebhookCallbackType.ON_EVENT:
            return on_event()
        if self is LinkDeliveryWebhookCallbackType.ON_EXIT:
            return on_exit()
