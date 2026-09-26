

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ParticipantDeclarationChangeDeliveryPartnerRequestDataType(enum.StrEnum):
    PARTICIPANT_DECLARATION = "participant-declaration"

    def visit(self, participant_declaration: typing.Callable[[], T_Result]) -> T_Result:
        if self is ParticipantDeclarationChangeDeliveryPartnerRequestDataType.PARTICIPANT_DECLARATION:
            return participant_declaration()
