

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ConsentRequestCustomerContactMethod(enum.StrEnum):
    """
    Bevorzugter Kontaktweg für Consent-Bestätigung
    """

    EMAIL = "email"
    SMS = "sms"
    APP = "app"
    POSTAL = "postal"

    def visit(
        self,
        email: typing.Callable[[], T_Result],
        sms: typing.Callable[[], T_Result],
        app: typing.Callable[[], T_Result],
        postal: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConsentRequestCustomerContactMethod.EMAIL:
            return email()
        if self is ConsentRequestCustomerContactMethod.SMS:
            return sms()
        if self is ConsentRequestCustomerContactMethod.APP:
            return app()
        if self is ConsentRequestCustomerContactMethod.POSTAL:
            return postal()
