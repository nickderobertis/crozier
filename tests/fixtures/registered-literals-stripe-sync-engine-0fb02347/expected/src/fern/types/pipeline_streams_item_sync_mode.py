

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PipelineStreamsItemSyncMode(enum.StrEnum):
    """
    How the source reads this stream. Defaults to full_refresh.
    """

    INCREMENTAL = "incremental"
    FULL_REFRESH = "full_refresh"

    def visit(
        self, incremental: typing.Callable[[], T_Result], full_refresh: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is PipelineStreamsItemSyncMode.INCREMENTAL:
            return incremental()
        if self is PipelineStreamsItemSyncMode.FULL_REFRESH:
            return full_refresh()
