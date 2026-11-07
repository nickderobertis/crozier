

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PossibleNormPartyScoreConstituentsEmail(enum.StrEnum):
    MATCHED = "Matched"
    MISMATCHED = "Mismatched"
    NOT_PROVIDED_BY_DATA_SOURCE = "Not_Provided_By_Data_Source"

    def visit(
        self,
        matched: typing.Callable[[], T_Result],
        mismatched: typing.Callable[[], T_Result],
        not_provided_by_data_source: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PossibleNormPartyScoreConstituentsEmail.MATCHED:
            return matched()
        if self is PossibleNormPartyScoreConstituentsEmail.MISMATCHED:
            return mismatched()
        if self is PossibleNormPartyScoreConstituentsEmail.NOT_PROVIDED_BY_DATA_SOURCE:
            return not_provided_by_data_source()
