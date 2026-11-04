

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DependencyEdgeToType(enum.StrEnum):
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
        if self is DependencyEdgeToType.DATA_SOURCE:
            return data_source()
        if self is DependencyEdgeToType.ASSET:
            return asset()
        if self is DependencyEdgeToType.WIDGET:
            return widget()
        if self is DependencyEdgeToType.LAYOUT:
            return layout()
        if self is DependencyEdgeToType.PLAYLIST:
            return playlist()
        if self is DependencyEdgeToType.CAMPAIGN:
            return campaign()
        if self is DependencyEdgeToType.SCHEDULE:
            return schedule()
        if self is DependencyEdgeToType.SCREEN_GROUP:
            return screen_group()
        if self is DependencyEdgeToType.SCREEN:
            return screen()
