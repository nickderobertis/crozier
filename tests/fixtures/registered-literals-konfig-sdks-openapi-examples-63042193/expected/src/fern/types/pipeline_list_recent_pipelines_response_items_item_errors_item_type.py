

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PipelineListRecentPipelinesResponseItemsItemErrorsItemType(enum.StrEnum):
    """
    The type of error.
    """

    CONFIG = "config"
    CONFIG_FETCH = "config-fetch"
    TIMEOUT = "timeout"
    PERMISSION = "permission"
    OTHER = "other"
    PLAN = "plan"

    def visit(
        self,
        config: typing.Callable[[], T_Result],
        config_fetch: typing.Callable[[], T_Result],
        timeout: typing.Callable[[], T_Result],
        permission: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
        plan: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PipelineListRecentPipelinesResponseItemsItemErrorsItemType.CONFIG:
            return config()
        if self is PipelineListRecentPipelinesResponseItemsItemErrorsItemType.CONFIG_FETCH:
            return config_fetch()
        if self is PipelineListRecentPipelinesResponseItemsItemErrorsItemType.TIMEOUT:
            return timeout()
        if self is PipelineListRecentPipelinesResponseItemsItemErrorsItemType.PERMISSION:
            return permission()
        if self is PipelineListRecentPipelinesResponseItemsItemErrorsItemType.OTHER:
            return other()
        if self is PipelineListRecentPipelinesResponseItemsItemErrorsItemType.PLAN:
            return plan()
