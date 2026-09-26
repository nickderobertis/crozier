

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CustomerPreferredContact(enum.StrEnum):
    """
    Channel preferred for follow-up. 'sms' is treated as text-message via 'phone'.
    """

    EMAIL = "email"
    PHONE = "phone"
    SMS = "sms"
    ANY = "any"

    def visit(
        self,
        email: typing.Callable[[], T_Result],
        phone: typing.Callable[[], T_Result],
        sms: typing.Callable[[], T_Result],
        any: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CustomerPreferredContact.EMAIL:
            return email()
        if self is CustomerPreferredContact.PHONE:
            return phone()
        if self is CustomerPreferredContact.SMS:
            return sms()
        if self is CustomerPreferredContact.ANY:
            return any()
