

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ToggleAssistantRequestChannelsItem(enum.StrEnum):
    PORTAL = "portal"
    CHAT = "chat"

    def visit(self, portal: typing.Callable[[], T_Result], chat: typing.Callable[[], T_Result]) -> T_Result:
        if self is ToggleAssistantRequestChannelsItem.PORTAL:
            return portal()
        if self is ToggleAssistantRequestChannelsItem.CHAT:
            return chat()
