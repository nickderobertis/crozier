

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BrandBugInputTargetScope(enum.StrEnum):
    ALL = "all"
    SCREENS = "screens"
    SYNC_GROUPS = "sync_groups"
    LOCATIONS = "locations"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        screens: typing.Callable[[], T_Result],
        sync_groups: typing.Callable[[], T_Result],
        locations: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BrandBugInputTargetScope.ALL:
            return all_()
        if self is BrandBugInputTargetScope.SCREENS:
            return screens()
        if self is BrandBugInputTargetScope.SYNC_GROUPS:
            return sync_groups()
        if self is BrandBugInputTargetScope.LOCATIONS:
            return locations()
