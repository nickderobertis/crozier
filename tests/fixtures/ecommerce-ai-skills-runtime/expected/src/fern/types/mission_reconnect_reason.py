

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MissionReconnectReason(enum.StrEnum):
    BACKLOG_LIMIT = "backlog_limit"
    LIFETIME_LIMIT = "lifetime_limit"

    def visit(
        self, backlog_limit: typing.Callable[[], T_Result], lifetime_limit: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is MissionReconnectReason.BACKLOG_LIMIT:
            return backlog_limit()
        if self is MissionReconnectReason.LIFETIME_LIMIT:
            return lifetime_limit()
