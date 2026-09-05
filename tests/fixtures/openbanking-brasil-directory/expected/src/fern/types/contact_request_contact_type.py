

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ContactRequestContactType(enum.StrEnum):
    """
    The type of Contact, default contact type is Business.
    """

    BUSINESS = "Business"
    TECHNICAL = "Technical"
    BILLING = "Billing"
    INCIDENT = "Incident"
    SECURITY = "Security"

    def visit(
        self,
        business: typing.Callable[[], T_Result],
        technical: typing.Callable[[], T_Result],
        billing: typing.Callable[[], T_Result],
        incident: typing.Callable[[], T_Result],
        security: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ContactRequestContactType.BUSINESS:
            return business()
        if self is ContactRequestContactType.TECHNICAL:
            return technical()
        if self is ContactRequestContactType.BILLING:
            return billing()
        if self is ContactRequestContactType.INCIDENT:
            return incident()
        if self is ContactRequestContactType.SECURITY:
            return security()
