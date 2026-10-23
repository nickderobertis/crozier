

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SurveyType(enum.StrEnum):
    """
    The type of the survey
    """

    LINK = "link"
    APP = "app"

    def visit(self, link: typing.Callable[[], T_Result], app: typing.Callable[[], T_Result]) -> T_Result:
        if self is SurveyType.LINK:
            return link()
        if self is SurveyType.APP:
            return app()
