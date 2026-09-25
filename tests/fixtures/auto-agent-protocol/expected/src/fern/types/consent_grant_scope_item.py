

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConsentGrantScopeItem(enum.StrEnum):
    LEAD_SUBMISSION = "lead_submission"

    def visit(self, lead_submission: typing.Callable[[], T_Result]) -> T_Result:
        if self is ConsentGrantScopeItem.LEAD_SUBMISSION:
            return lead_submission()
