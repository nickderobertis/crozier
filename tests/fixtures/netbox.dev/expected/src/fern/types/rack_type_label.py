

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RackTypeLabel(enum.StrEnum):
    TWO_POST_FRAME = "2-post frame"
    FOUR_POST_FRAME = "4-post frame"
    FOUR_POST_CABINET = "4-post cabinet"
    WALL_MOUNTED_FRAME = "Wall-mounted frame"
    WALL_MOUNTED_FRAME_VERTICAL = "Wall-mounted frame (vertical)"
    WALL_MOUNTED_CABINET = "Wall-mounted cabinet"
    WALL_MOUNTED_CABINET_VERTICAL = "Wall-mounted cabinet (vertical)"

    def visit(
        self,
        two_post_frame: typing.Callable[[], T_Result],
        four_post_frame: typing.Callable[[], T_Result],
        four_post_cabinet: typing.Callable[[], T_Result],
        wall_mounted_frame: typing.Callable[[], T_Result],
        wall_mounted_frame_vertical: typing.Callable[[], T_Result],
        wall_mounted_cabinet: typing.Callable[[], T_Result],
        wall_mounted_cabinet_vertical: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RackTypeLabel.TWO_POST_FRAME:
            return two_post_frame()
        if self is RackTypeLabel.FOUR_POST_FRAME:
            return four_post_frame()
        if self is RackTypeLabel.FOUR_POST_CABINET:
            return four_post_cabinet()
        if self is RackTypeLabel.WALL_MOUNTED_FRAME:
            return wall_mounted_frame()
        if self is RackTypeLabel.WALL_MOUNTED_FRAME_VERTICAL:
            return wall_mounted_frame_vertical()
        if self is RackTypeLabel.WALL_MOUNTED_CABINET:
            return wall_mounted_cabinet()
        if self is RackTypeLabel.WALL_MOUNTED_CABINET_VERTICAL:
            return wall_mounted_cabinet_vertical()
