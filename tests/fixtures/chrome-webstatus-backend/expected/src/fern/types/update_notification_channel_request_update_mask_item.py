

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateNotificationChannelRequestUpdateMaskItem(enum.StrEnum):
    NAME = "name"
    CONFIG = "config"

    def visit(self, name: typing.Callable[[], T_Result], config: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdateNotificationChannelRequestUpdateMaskItem.NAME:
            return name()
        if self is UpdateNotificationChannelRequestUpdateMaskItem.CONFIG:
            return config()
