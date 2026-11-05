

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DependencyEdgeFromType(enum.StrEnum):
    DATA_SOURCE = "data_source"
    ASSET = "asset"
    WIDGET = "widget"
    LAYOUT = "layout"
    PLAYLIST = "playlist"
    CAMPAIGN = "campaign"
    SCHEDULE = "schedule"
    SCREEN_GROUP = "screen_group"
    SCREEN = "screen"

    def visit(
        self,
        data_source: typing.Callable[[], T_Result],
        asset: typing.Callable[[], T_Result],
        widget: typing.Callable[[], T_Result],
        layout: typing.Callable[[], T_Result],
        playlist: typing.Callable[[], T_Result],
        campaign: typing.Callable[[], T_Result],
        schedule: typing.Callable[[], T_Result],
        screen_group: typing.Callable[[], T_Result],
        screen: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DependencyEdgeFromType.DATA_SOURCE:
            return data_source()
        if self is DependencyEdgeFromType.ASSET:
            return asset()
        if self is DependencyEdgeFromType.WIDGET:
            return widget()
        if self is DependencyEdgeFromType.LAYOUT:
            return layout()
        if self is DependencyEdgeFromType.PLAYLIST:
            return playlist()
        if self is DependencyEdgeFromType.CAMPAIGN:
            return campaign()
        if self is DependencyEdgeFromType.SCHEDULE:
            return schedule()
        if self is DependencyEdgeFromType.SCREEN_GROUP:
            return screen_group()
        if self is DependencyEdgeFromType.SCREEN:
            return screen()
