

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CourseEditionResponseUnsupportedReason(enum.StrEnum):
    SAME_LANGUAGE = "sameLanguage"
    FORMAT = "format"
    LANGUAGE = "language"
    UNAVAILABLE = "unavailable"

    def visit(
        self,
        same_language: typing.Callable[[], T_Result],
        format: typing.Callable[[], T_Result],
        language: typing.Callable[[], T_Result],
        unavailable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CourseEditionResponseUnsupportedReason.SAME_LANGUAGE:
            return same_language()
        if self is CourseEditionResponseUnsupportedReason.FORMAT:
            return format()
        if self is CourseEditionResponseUnsupportedReason.LANGUAGE:
            return language()
        if self is CourseEditionResponseUnsupportedReason.UNAVAILABLE:
            return unavailable()
