

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PossibleNormLawFirmScoreConstituentsSecretaryOfStateId(enum.StrEnum):
    MATCHED = "Matched"
    MISMATCHED = "Mismatched"
    NOT_PROVIDED_BY_DATA_SOURCE = "Not_Provided_By_Data_Source"

    def visit(
        self,
        matched: typing.Callable[[], T_Result],
        mismatched: typing.Callable[[], T_Result],
        not_provided_by_data_source: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PossibleNormLawFirmScoreConstituentsSecretaryOfStateId.MATCHED:
            return matched()
        if self is PossibleNormLawFirmScoreConstituentsSecretaryOfStateId.MISMATCHED:
            return mismatched()
        if self is PossibleNormLawFirmScoreConstituentsSecretaryOfStateId.NOT_PROVIDED_BY_DATA_SOURCE:
            return not_provided_by_data_source()
