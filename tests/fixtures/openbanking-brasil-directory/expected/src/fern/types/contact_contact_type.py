

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ContactContactType(enum.StrEnum):
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
        if self is ContactContactType.BUSINESS:
            return business()
        if self is ContactContactType.TECHNICAL:
            return technical()
        if self is ContactContactType.BILLING:
            return billing()
        if self is ContactContactType.INCIDENT:
            return incident()
        if self is ContactContactType.SECURITY:
            return security()
