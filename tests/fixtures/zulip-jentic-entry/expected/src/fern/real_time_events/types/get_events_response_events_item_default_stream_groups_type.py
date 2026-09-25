

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemDefaultStreamGroupsType(enum.StrEnum):
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    DEFAULT_STREAM_GROUPS = "default_stream_groups"

    def visit(self, default_stream_groups: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemDefaultStreamGroupsType.DEFAULT_STREAM_GROUPS:
            return default_stream_groups()
