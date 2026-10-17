

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ThreadSearchRequestSelectItem(enum.StrEnum):
    THREAD_ID = "thread_id"
    CREATED_AT = "created_at"
    UPDATED_AT = "updated_at"
    STATE_UPDATED_AT = "state_updated_at"
    METADATA = "metadata"
    CONFIG = "config"
    STATUS = "status"
    VALUES = "values"
    INTERRUPTS = "interrupts"

    def visit(
        self,
        thread_id: typing.Callable[[], T_Result],
        created_at: typing.Callable[[], T_Result],
        updated_at: typing.Callable[[], T_Result],
        state_updated_at: typing.Callable[[], T_Result],
        metadata: typing.Callable[[], T_Result],
        config: typing.Callable[[], T_Result],
        status: typing.Callable[[], T_Result],
        values: typing.Callable[[], T_Result],
        interrupts: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ThreadSearchRequestSelectItem.THREAD_ID:
            return thread_id()
        if self is ThreadSearchRequestSelectItem.CREATED_AT:
            return created_at()
        if self is ThreadSearchRequestSelectItem.UPDATED_AT:
            return updated_at()
        if self is ThreadSearchRequestSelectItem.STATE_UPDATED_AT:
            return state_updated_at()
        if self is ThreadSearchRequestSelectItem.METADATA:
            return metadata()
        if self is ThreadSearchRequestSelectItem.CONFIG:
            return config()
        if self is ThreadSearchRequestSelectItem.STATUS:
            return status()
        if self is ThreadSearchRequestSelectItem.VALUES:
            return values()
        if self is ThreadSearchRequestSelectItem.INTERRUPTS:
            return interrupts()
