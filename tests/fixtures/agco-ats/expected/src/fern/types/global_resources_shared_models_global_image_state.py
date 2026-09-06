

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GlobalResourcesSharedModelsGlobalImageState(enum.StrEnum):
    """
    Indicates the state of this file. Must be 'Created' when created. Read Only.
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
        if self is GlobalResourcesSharedModelsGlobalImageState.CREATED:
            return created()
        if self is GlobalResourcesSharedModelsGlobalImageState.AVAILABLE:
            return available()
        if self is GlobalResourcesSharedModelsGlobalImageState.REMOVED:
            return removed()
