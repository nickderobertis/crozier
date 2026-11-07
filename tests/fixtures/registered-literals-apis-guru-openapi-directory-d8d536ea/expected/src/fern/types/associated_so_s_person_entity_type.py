

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AssociatedSoSPersonEntityType(enum.StrEnum):
    PARTNER = "Partner"
    AGENT = "Agent"
    CEO = "CEO"
    PARTNER_GENERAL_MEMBER = "Partner/General Member"

    def visit(
        self,
        partner: typing.Callable[[], T_Result],
        agent: typing.Callable[[], T_Result],
        ceo: typing.Callable[[], T_Result],
        partner_general_member: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AssociatedSoSPersonEntityType.PARTNER:
            return partner()
        if self is AssociatedSoSPersonEntityType.AGENT:
            return agent()
        if self is AssociatedSoSPersonEntityType.CEO:
            return ceo()
        if self is AssociatedSoSPersonEntityType.PARTNER_GENERAL_MEMBER:
            return partner_general_member()
