

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostPositionsRequestCategory(enum.StrEnum):
    EXPERIENCE = "Experience"
    EDUCATION = "Education"
    AWARDS = "Awards"
    AFFILIATIONS = "Affiliations"
    PORTFOLIO = "Portfolio"

    def visit(
        self,
        experience: typing.Callable[[], T_Result],
        education: typing.Callable[[], T_Result],
        awards: typing.Callable[[], T_Result],
        affiliations: typing.Callable[[], T_Result],
        portfolio: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostPositionsRequestCategory.EXPERIENCE:
            return experience()
        if self is PostPositionsRequestCategory.EDUCATION:
            return education()
        if self is PostPositionsRequestCategory.AWARDS:
            return awards()
        if self is PostPositionsRequestCategory.AFFILIATIONS:
            return affiliations()
        if self is PostPositionsRequestCategory.PORTFOLIO:
            return portfolio()
