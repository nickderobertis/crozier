

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WritableRackType(enum.StrEnum):
    TWO_POST_FRAME = "2-post-frame"
    FOUR_POST_FRAME = "4-post-frame"
    FOUR_POST_CABINET = "4-post-cabinet"
    WALL_FRAME = "wall-frame"
    WALL_FRAME_VERTICAL = "wall-frame-vertical"
    WALL_CABINET = "wall-cabinet"
    WALL_CABINET_VERTICAL = "wall-cabinet-vertical"

    def visit(
        self,
        two_post_frame: typing.Callable[[], T_Result],
        four_post_frame: typing.Callable[[], T_Result],
        four_post_cabinet: typing.Callable[[], T_Result],
        wall_frame: typing.Callable[[], T_Result],
        wall_frame_vertical: typing.Callable[[], T_Result],
        wall_cabinet: typing.Callable[[], T_Result],
        wall_cabinet_vertical: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WritableRackType.TWO_POST_FRAME:
            return two_post_frame()
        if self is WritableRackType.FOUR_POST_FRAME:
            return four_post_frame()
        if self is WritableRackType.FOUR_POST_CABINET:
            return four_post_cabinet()
        if self is WritableRackType.WALL_FRAME:
            return wall_frame()
        if self is WritableRackType.WALL_FRAME_VERTICAL:
            return wall_frame_vertical()
        if self is WritableRackType.WALL_CABINET:
            return wall_cabinet()
        if self is WritableRackType.WALL_CABINET_VERTICAL:
            return wall_cabinet_vertical()
