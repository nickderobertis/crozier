

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PossibleNormLawFirmSourceDetailsSource(enum.StrEnum):
    CASE_ATTORNEY_LINKED_IN_OTHER_CASES = "Case_Attorney_Linked_In_Other_Cases"
    CASE_ATTORNEY_FIELD_CONTAINS_LAW_FIRM = "Case_Attorney_Field_Contains_Law_Firm"

    def visit(
        self,
        case_attorney_linked_in_other_cases: typing.Callable[[], T_Result],
        case_attorney_field_contains_law_firm: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PossibleNormLawFirmSourceDetailsSource.CASE_ATTORNEY_LINKED_IN_OTHER_CASES:
            return case_attorney_linked_in_other_cases()
        if self is PossibleNormLawFirmSourceDetailsSource.CASE_ATTORNEY_FIELD_CONTAINS_LAW_FIRM:
            return case_attorney_field_contains_law_firm()
