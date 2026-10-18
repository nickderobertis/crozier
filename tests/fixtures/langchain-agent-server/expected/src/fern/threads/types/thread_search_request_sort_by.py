

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ThreadSearchRequestSortBy(enum.StrEnum):
    """
    Sort by field.
    """

    THREAD_ID = "thread_id"
    STATUS = "status"
    CREATED_AT = "created_at"
    UPDATED_AT = "updated_at"
    STATE_UPDATED_AT = "state_updated_at"

    def visit(
        self,
        thread_id: typing.Callable[[], T_Result],
        status: typing.Callable[[], T_Result],
        created_at: typing.Callable[[], T_Result],
        updated_at: typing.Callable[[], T_Result],
        state_updated_at: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ThreadSearchRequestSortBy.THREAD_ID:
            return thread_id()
        if self is ThreadSearchRequestSortBy.STATUS:
            return status()
        if self is ThreadSearchRequestSortBy.CREATED_AT:
            return created_at()
        if self is ThreadSearchRequestSortBy.UPDATED_AT:
            return updated_at()
        if self is ThreadSearchRequestSortBy.STATE_UPDATED_AT:
            return state_updated_at()
