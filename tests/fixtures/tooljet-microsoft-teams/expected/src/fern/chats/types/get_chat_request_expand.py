

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetChatRequestExpand(enum.StrEnum):
    MEMBERS = "members"
    INSTALLED_APPS = "installedApps"
    LAST_MESSAGE_PREVIEW = "lastMessagePreview"

    def visit(
        self,
        members: typing.Callable[[], T_Result],
        installed_apps: typing.Callable[[], T_Result],
        last_message_preview: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetChatRequestExpand.MEMBERS:
            return members()
        if self is GetChatRequestExpand.INSTALLED_APPS:
            return installed_apps()
        if self is GetChatRequestExpand.LAST_MESSAGE_PREVIEW:
            return last_message_preview()
