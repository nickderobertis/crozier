

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HitlDecisionInputAction(enum.StrEnum):
    APPROVE = "approve"
    EDIT = "edit"
    REJECT = "reject"

    def visit(
        self,
        approve: typing.Callable[[], T_Result],
        edit: typing.Callable[[], T_Result],
        reject: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is HitlDecisionInputAction.APPROVE:
            return approve()
        if self is HitlDecisionInputAction.EDIT:
            return edit()
        if self is HitlDecisionInputAction.REJECT:
            return reject()
