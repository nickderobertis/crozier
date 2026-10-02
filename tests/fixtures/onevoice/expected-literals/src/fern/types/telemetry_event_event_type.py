

import typing

TelemetryEventEventType = typing.Union[
    typing.Literal["page_view", "api_error", "chat_send", "button_click", "activation", "approval", "value_recap"],
    typing.Any,
]
