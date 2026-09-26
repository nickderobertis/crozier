

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ParticipantDeclarationAttributesIneligibleForFundingReason(enum.StrEnum):
    """
    If the declaration is ineligible, the reason why
    """

    DUPLICATE_DECLARATION = "duplicate_declaration"

    def visit(self, duplicate_declaration: typing.Callable[[], T_Result]) -> T_Result:
        if self is ParticipantDeclarationAttributesIneligibleForFundingReason.DUPLICATE_DECLARATION:
            return duplicate_declaration()
