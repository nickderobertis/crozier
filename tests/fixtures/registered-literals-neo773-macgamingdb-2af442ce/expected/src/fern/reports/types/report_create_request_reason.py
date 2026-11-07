

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ReportCreateRequestReason(enum.StrEnum):
    SPAM = "spam"
    OFFENSIVE = "offensive"
    OFF_TOPIC = "off_topic"
    FAKE = "fake"
    OTHER = "other"

    def visit(
        self,
        spam: typing.Callable[[], T_Result],
        offensive: typing.Callable[[], T_Result],
        off_topic: typing.Callable[[], T_Result],
        fake: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ReportCreateRequestReason.SPAM:
            return spam()
        if self is ReportCreateRequestReason.OFFENSIVE:
            return offensive()
        if self is ReportCreateRequestReason.OFF_TOPIC:
            return off_topic()
        if self is ReportCreateRequestReason.FAKE:
            return fake()
        if self is ReportCreateRequestReason.OTHER:
            return other()
