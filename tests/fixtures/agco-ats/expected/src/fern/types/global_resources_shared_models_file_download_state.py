

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GlobalResourcesSharedModelsFileDownloadState(enum.StrEnum):
    """
    Indicates the state of this file. Must be 'Created' when created.
    """

    CREATED = "Created"
    AVAILABLE = "Available"
    REMOVED = "Removed"

    def visit(
        self,
        created: typing.Callable[[], T_Result],
        available: typing.Callable[[], T_Result],
        removed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GlobalResourcesSharedModelsFileDownloadState.CREATED:
            return created()
        if self is GlobalResourcesSharedModelsFileDownloadState.AVAILABLE:
            return available()
        if self is GlobalResourcesSharedModelsFileDownloadState.REMOVED:
            return removed()
