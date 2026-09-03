

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AgeVerificationResponseAttributeValue(enum.StrEnum):
    """
    Attribut-only Antwort
    """

    YES = "YES"
    NO = "NO"

    def visit(self, yes: typing.Callable[[], T_Result], no: typing.Callable[[], T_Result]) -> T_Result:
        if self is AgeVerificationResponseAttributeValue.YES:
            return yes()
        if self is AgeVerificationResponseAttributeValue.NO:
            return no()
