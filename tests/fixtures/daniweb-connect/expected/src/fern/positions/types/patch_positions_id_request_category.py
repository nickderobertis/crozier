

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PatchPositionsIdRequestCategory(enum.StrEnum):
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
        if self is PatchPositionsIdRequestCategory.EXPERIENCE:
            return experience()
        if self is PatchPositionsIdRequestCategory.EDUCATION:
            return education()
        if self is PatchPositionsIdRequestCategory.AWARDS:
            return awards()
        if self is PatchPositionsIdRequestCategory.AFFILIATIONS:
            return affiliations()
        if self is PatchPositionsIdRequestCategory.PORTFOLIO:
            return portfolio()
