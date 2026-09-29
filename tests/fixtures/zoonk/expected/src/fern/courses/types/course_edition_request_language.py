

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CourseEditionRequestLanguage(enum.StrEnum):
    """
    Requested instructional language
    """

    EN = "en"
    ES = "es"
    PT = "pt"
    FR = "fr"
    DE = "de"

    def visit(
        self,
        en: typing.Callable[[], T_Result],
        es: typing.Callable[[], T_Result],
        pt: typing.Callable[[], T_Result],
        fr: typing.Callable[[], T_Result],
        de: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CourseEditionRequestLanguage.EN:
            return en()
        if self is CourseEditionRequestLanguage.ES:
            return es()
        if self is CourseEditionRequestLanguage.PT:
            return pt()
        if self is CourseEditionRequestLanguage.FR:
            return fr()
        if self is CourseEditionRequestLanguage.DE:
            return de()
