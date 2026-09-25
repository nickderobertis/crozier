

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RespondentCountryBlockGroupType(enum.StrEnum):
    RESPONDENT_COUNTRY = "RESPONDENT_COUNTRY"

    def visit(self, respondent_country: typing.Callable[[], T_Result]) -> T_Result:
        if self is RespondentCountryBlockGroupType.RESPONDENT_COUNTRY:
            return respondent_country()
