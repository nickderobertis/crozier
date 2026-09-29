

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetCourseEditionRequestLanguage(enum.StrEnum):
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
        if self is GetCourseEditionRequestLanguage.EN:
            return en()
        if self is GetCourseEditionRequestLanguage.ES:
            return es()
        if self is GetCourseEditionRequestLanguage.PT:
            return pt()
        if self is GetCourseEditionRequestLanguage.FR:
            return fr()
        if self is GetCourseEditionRequestLanguage.DE:
            return de()
