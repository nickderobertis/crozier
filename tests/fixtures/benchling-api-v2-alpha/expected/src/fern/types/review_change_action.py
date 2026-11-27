

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReviewChangeAction(enum.StrEnum):
    """
    The action which was performed with this change
    """

    SEND_FOR_REVIEW = "SEND_FOR_REVIEW"
    ACCEPT = "ACCEPT"
    REJECT = "REJECT"
    COMMENT = "COMMENT"
    RETRACT = "RETRACT"

    def visit(
        self,
        send_for_review: typing.Callable[[], T_Result],
        accept: typing.Callable[[], T_Result],
        reject: typing.Callable[[], T_Result],
        comment: typing.Callable[[], T_Result],
        retract: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ReviewChangeAction.SEND_FOR_REVIEW:
            return send_for_review()
        if self is ReviewChangeAction.ACCEPT:
            return accept()
        if self is ReviewChangeAction.REJECT:
            return reject()
        if self is ReviewChangeAction.COMMENT:
            return comment()
        if self is ReviewChangeAction.RETRACT:
            return retract()
