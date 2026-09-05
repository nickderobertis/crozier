

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetConversationsStatusesRequestFilter(enum.StrEnum):
    NEW = "new"
    INTRODUCTIONS = "introductions"
    UNREPLIED = "unreplied"
    NOTIFICATIONS = "notifications"

    def visit(
        self,
        new: typing.Callable[[], T_Result],
        introductions: typing.Callable[[], T_Result],
        unreplied: typing.Callable[[], T_Result],
        notifications: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetConversationsStatusesRequestFilter.NEW:
            return new()
        if self is GetConversationsStatusesRequestFilter.INTRODUCTIONS:
            return introductions()
        if self is GetConversationsStatusesRequestFilter.UNREPLIED:
            return unreplied()
        if self is GetConversationsStatusesRequestFilter.NOTIFICATIONS:
            return notifications()
