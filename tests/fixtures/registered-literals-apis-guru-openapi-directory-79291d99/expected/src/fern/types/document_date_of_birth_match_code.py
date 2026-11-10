

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocumentDateOfBirthMatchCode(enum.StrEnum):
    """
    A match summary describing the cross comparison between the subject's date of birth, extracted from the document image, and the date of birth they separately provided to the identity verification attempt.
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
        if self is DocumentDateOfBirthMatchCode.MATCH:
            return match()
        if self is DocumentDateOfBirthMatchCode.PARTIAL_MATCH:
            return partial_match()
        if self is DocumentDateOfBirthMatchCode.NO_MATCH:
            return no_match()
