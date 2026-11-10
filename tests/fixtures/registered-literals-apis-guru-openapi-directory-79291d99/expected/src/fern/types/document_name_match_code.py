

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocumentNameMatchCode(enum.StrEnum):
    """
    A match summary describing the cross comparison between the subject's name, extracted from the document image, and the name they separately provided to identity verification attempt.
    """

    MATCH = "match"
    PARTIAL_MATCH = "partial_match"
    NO_MATCH = "no_match"

    def visit(
        self,
        match: typing.Callable[[], T_Result],
        partial_match: typing.Callable[[], T_Result],
        no_match: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocumentNameMatchCode.MATCH:
            return match()
        if self is DocumentNameMatchCode.PARTIAL_MATCH:
            return partial_match()
        if self is DocumentNameMatchCode.NO_MATCH:
            return no_match()
