

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RiskProfileEsgPreferencesEsgImportance(enum.StrEnum):
    NOT_IMPORTANT = "not_important"
    SOMEWHAT_IMPORTANT = "somewhat_important"
    VERY_IMPORTANT = "very_important"

    def visit(
        self,
        not_important: typing.Callable[[], T_Result],
        somewhat_important: typing.Callable[[], T_Result],
        very_important: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RiskProfileEsgPreferencesEsgImportance.NOT_IMPORTANT:
            return not_important()
        if self is RiskProfileEsgPreferencesEsgImportance.SOMEWHAT_IMPORTANT:
            return somewhat_important()
        if self is RiskProfileEsgPreferencesEsgImportance.VERY_IMPORTANT:
            return very_important()
