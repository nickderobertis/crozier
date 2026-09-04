

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ContactInformationPreferredContactMethod(enum.StrEnum):
    EMAIL = "email"
    SMS = "sms"
    PHONE = "phone"
    POSTAL = "postal"
    APP = "app"

    def visit(
        self,
        email: typing.Callable[[], T_Result],
        sms: typing.Callable[[], T_Result],
        phone: typing.Callable[[], T_Result],
        postal: typing.Callable[[], T_Result],
        app: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ContactInformationPreferredContactMethod.EMAIL:
            return email()
        if self is ContactInformationPreferredContactMethod.SMS:
            return sms()
        if self is ContactInformationPreferredContactMethod.PHONE:
            return phone()
        if self is ContactInformationPreferredContactMethod.POSTAL:
            return postal()
        if self is ContactInformationPreferredContactMethod.APP:
            return app()
