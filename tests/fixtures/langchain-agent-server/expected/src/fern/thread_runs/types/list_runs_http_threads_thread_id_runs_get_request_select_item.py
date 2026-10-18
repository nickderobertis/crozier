

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListRunsHttpThreadsThreadIdRunsGetRequestSelectItem(enum.StrEnum):
    RUN_ID = "run_id"
    THREAD_ID = "thread_id"
    ASSISTANT_ID = "assistant_id"
    CREATED_AT = "created_at"
    UPDATED_AT = "updated_at"
    STATUS = "status"
    METADATA = "metadata"
    KWARGS = "kwargs"
    MULTITASK_STRATEGY = "multitask_strategy"
    LANGSMITH_SESSION_NAME = "langsmith_session_name"

    def visit(
        self,
        run_id: typing.Callable[[], T_Result],
        thread_id: typing.Callable[[], T_Result],
        assistant_id: typing.Callable[[], T_Result],
        created_at: typing.Callable[[], T_Result],
        updated_at: typing.Callable[[], T_Result],
        status: typing.Callable[[], T_Result],
        metadata: typing.Callable[[], T_Result],
        kwargs_: typing.Callable[[], T_Result],
        multitask_strategy: typing.Callable[[], T_Result],
        langsmith_session_name: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListRunsHttpThreadsThreadIdRunsGetRequestSelectItem.RUN_ID:
            return run_id()
        if self is ListRunsHttpThreadsThreadIdRunsGetRequestSelectItem.THREAD_ID:
            return thread_id()
        if self is ListRunsHttpThreadsThreadIdRunsGetRequestSelectItem.ASSISTANT_ID:
            return assistant_id()
        if self is ListRunsHttpThreadsThreadIdRunsGetRequestSelectItem.CREATED_AT:
            return created_at()
        if self is ListRunsHttpThreadsThreadIdRunsGetRequestSelectItem.UPDATED_AT:
            return updated_at()
        if self is ListRunsHttpThreadsThreadIdRunsGetRequestSelectItem.STATUS:
            return status()
        if self is ListRunsHttpThreadsThreadIdRunsGetRequestSelectItem.METADATA:
            return metadata()
        if self is ListRunsHttpThreadsThreadIdRunsGetRequestSelectItem.KWARGS:
            return kwargs_()
        if self is ListRunsHttpThreadsThreadIdRunsGetRequestSelectItem.MULTITASK_STRATEGY:
            return multitask_strategy()
        if self is ListRunsHttpThreadsThreadIdRunsGetRequestSelectItem.LANGSMITH_SESSION_NAME:
            return langsmith_session_name()
