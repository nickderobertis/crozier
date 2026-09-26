

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemChannelFolderType(enum.StrEnum):
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    CHANNEL_FOLDER = "channel_folder"

    def visit(self, channel_folder: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemChannelFolderType.CHANNEL_FOLDER:
            return channel_folder()
