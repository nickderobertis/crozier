

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetTeamRequestExpand(enum.StrEnum):
    MEMBERS = "members"
    CHANNELS = "channels"
    INSTALLED_APPS = "installedApps"
    SCHEDULE = "schedule"

    def visit(
        self,
        members: typing.Callable[[], T_Result],
        channels: typing.Callable[[], T_Result],
        installed_apps: typing.Callable[[], T_Result],
        schedule: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetTeamRequestExpand.MEMBERS:
            return members()
        if self is GetTeamRequestExpand.CHANNELS:
            return channels()
        if self is GetTeamRequestExpand.INSTALLED_APPS:
            return installed_apps()
        if self is GetTeamRequestExpand.SCHEDULE:
            return schedule()
