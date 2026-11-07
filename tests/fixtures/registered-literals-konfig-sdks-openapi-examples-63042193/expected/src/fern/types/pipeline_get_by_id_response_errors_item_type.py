

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PipelineGetByIdResponseErrorsItemType(enum.StrEnum):
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
        if self is PipelineGetByIdResponseErrorsItemType.CONFIG:
            return config()
        if self is PipelineGetByIdResponseErrorsItemType.CONFIG_FETCH:
            return config_fetch()
        if self is PipelineGetByIdResponseErrorsItemType.TIMEOUT:
            return timeout()
        if self is PipelineGetByIdResponseErrorsItemType.PERMISSION:
            return permission()
        if self is PipelineGetByIdResponseErrorsItemType.OTHER:
            return other()
        if self is PipelineGetByIdResponseErrorsItemType.PLAN:
            return plan()
