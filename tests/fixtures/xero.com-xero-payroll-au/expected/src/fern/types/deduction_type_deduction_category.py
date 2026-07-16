

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DeductionTypeDeductionCategory(enum.StrEnum):
    NONE = "NONE"
    UNIONFEES = "UNIONFEES"
    WORKPLACEGIVING = "WORKPLACEGIVING"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        unionfees: typing.Callable[[], T_Result],
        workplacegiving: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DeductionTypeDeductionCategory.NONE:
            return none()
        if self is DeductionTypeDeductionCategory.UNIONFEES:
            return unionfees()
        if self is DeductionTypeDeductionCategory.WORKPLACEGIVING:
            return workplacegiving()
