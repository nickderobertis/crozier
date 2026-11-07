

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DependencyNodeType(enum.StrEnum):
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
        if self is DependencyNodeType.DATA_SOURCE:
            return data_source()
        if self is DependencyNodeType.ASSET:
            return asset()
        if self is DependencyNodeType.WIDGET:
            return widget()
        if self is DependencyNodeType.LAYOUT:
            return layout()
        if self is DependencyNodeType.PLAYLIST:
            return playlist()
        if self is DependencyNodeType.CAMPAIGN:
            return campaign()
        if self is DependencyNodeType.SCHEDULE:
            return schedule()
        if self is DependencyNodeType.SCREEN_GROUP:
            return screen_group()
        if self is DependencyNodeType.SCREEN:
            return screen()
