

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NoiseMeterInputTargetScope(enum.StrEnum):
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
        if self is NoiseMeterInputTargetScope.ALL:
            return all_()
        if self is NoiseMeterInputTargetScope.SCREENS:
            return screens()
        if self is NoiseMeterInputTargetScope.SYNC_GROUPS:
            return sync_groups()
        if self is NoiseMeterInputTargetScope.LOCATIONS:
            return locations()
