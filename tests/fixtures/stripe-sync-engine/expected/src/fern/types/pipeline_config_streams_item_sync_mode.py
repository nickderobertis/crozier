

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PipelineConfigStreamsItemSyncMode(enum.StrEnum):
    """
    How the source reads this stream. Defaults to full_refresh.
    """

    INCREMENTAL = "incremental"
    FULL_REFRESH = "full_refresh"

    def visit(
        self, incremental: typing.Callable[[], T_Result], full_refresh: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is PipelineConfigStreamsItemSyncMode.INCREMENTAL:
            return incremental()
        if self is PipelineConfigStreamsItemSyncMode.FULL_REFRESH:
            return full_refresh()
