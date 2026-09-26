

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ParticipantDeclarationChangeDeliveryPartnerRequestDataAttributesDeclarationType(enum.StrEnum):
    """
    The event declaration type
    """

    COMPLETED = "completed"

    def visit(self, completed: typing.Callable[[], T_Result]) -> T_Result:
        if self is ParticipantDeclarationChangeDeliveryPartnerRequestDataAttributesDeclarationType.COMPLETED:
            return completed()
