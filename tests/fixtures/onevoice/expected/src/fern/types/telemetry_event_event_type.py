

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TelemetryEventEventType(enum.StrEnum):
    PAGE_VIEW = "page_view"
    API_ERROR = "api_error"
    CHAT_SEND = "chat_send"
    BUTTON_CLICK = "button_click"
    ACTIVATION = "activation"
    APPROVAL = "approval"
    VALUE_RECAP = "value_recap"

    def visit(
        self,
        page_view: typing.Callable[[], T_Result],
        api_error: typing.Callable[[], T_Result],
        chat_send: typing.Callable[[], T_Result],
        button_click: typing.Callable[[], T_Result],
        activation: typing.Callable[[], T_Result],
        approval: typing.Callable[[], T_Result],
        value_recap: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TelemetryEventEventType.PAGE_VIEW:
            return page_view()
        if self is TelemetryEventEventType.API_ERROR:
            return api_error()
        if self is TelemetryEventEventType.CHAT_SEND:
            return chat_send()
        if self is TelemetryEventEventType.BUTTON_CLICK:
            return button_click()
        if self is TelemetryEventEventType.ACTIVATION:
            return activation()
        if self is TelemetryEventEventType.APPROVAL:
            return approval()
        if self is TelemetryEventEventType.VALUE_RECAP:
            return value_recap()
