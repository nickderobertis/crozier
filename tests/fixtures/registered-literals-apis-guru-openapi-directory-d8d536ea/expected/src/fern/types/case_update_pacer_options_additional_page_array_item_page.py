

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CaseUpdatePacerOptionsAdditionalPageArrayItemPage(enum.StrEnum):
    ASSOCIATED_CASES = "associatedCases"
    CASE_SUMMARY = "caseSummary"
    LIST_OF_CREDITORS = "listOfCreditors"

    def visit(
        self,
        associated_cases: typing.Callable[[], T_Result],
        case_summary: typing.Callable[[], T_Result],
        list_of_creditors: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CaseUpdatePacerOptionsAdditionalPageArrayItemPage.ASSOCIATED_CASES:
            return associated_cases()
        if self is CaseUpdatePacerOptionsAdditionalPageArrayItemPage.CASE_SUMMARY:
            return case_summary()
        if self is CaseUpdatePacerOptionsAdditionalPageArrayItemPage.LIST_OF_CREDITORS:
            return list_of_creditors()
