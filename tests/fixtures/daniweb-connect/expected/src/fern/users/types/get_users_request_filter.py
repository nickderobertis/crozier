

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetUsersRequestFilter(enum.StrEnum):
    CONNECTIONS = "connections"
    MATCHES = "matches"
    SKIPPED = "skipped"
    MUTED = "muted"

    def visit(
        self,
        connections: typing.Callable[[], T_Result],
        matches: typing.Callable[[], T_Result],
        skipped: typing.Callable[[], T_Result],
        muted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetUsersRequestFilter.CONNECTIONS:
            return connections()
        if self is GetUsersRequestFilter.MATCHES:
            return matches()
        if self is GetUsersRequestFilter.SKIPPED:
            return skipped()
        if self is GetUsersRequestFilter.MUTED:
            return muted()
