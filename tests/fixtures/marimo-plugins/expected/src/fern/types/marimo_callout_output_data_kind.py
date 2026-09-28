

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarimoCalloutOutputDataKind(enum.StrEnum):
    NEUTRAL = "neutral"
    SUCCESS = "success"
    WARN = "warn"
    DANGER = "danger"
    INFO = "info"
    ALERT = "alert"

    def visit(
        self,
        neutral: typing.Callable[[], T_Result],
        success: typing.Callable[[], T_Result],
        warn: typing.Callable[[], T_Result],
        danger: typing.Callable[[], T_Result],
        info: typing.Callable[[], T_Result],
        alert: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MarimoCalloutOutputDataKind.NEUTRAL:
            return neutral()
        if self is MarimoCalloutOutputDataKind.SUCCESS:
            return success()
        if self is MarimoCalloutOutputDataKind.WARN:
            return warn()
        if self is MarimoCalloutOutputDataKind.DANGER:
            return danger()
        if self is MarimoCalloutOutputDataKind.INFO:
            return info()
        if self is MarimoCalloutOutputDataKind.ALERT:
            return alert()
