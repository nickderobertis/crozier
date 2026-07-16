

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObReadConsentResponse1DataStatus(enum.StrEnum):
    """
    Specifies the status of consent resource in code form.
    """

    AUTHORISED = "Authorised"
    AWAITING_AUTHORISATION = "AwaitingAuthorisation"
    REJECTED = "Rejected"
    REVOKED = "Revoked"

    def visit(
        self,
        authorised: typing.Callable[[], T_Result],
        awaiting_authorisation: typing.Callable[[], T_Result],
        rejected: typing.Callable[[], T_Result],
        revoked: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObReadConsentResponse1DataStatus.AUTHORISED:
            return authorised()
        if self is ObReadConsentResponse1DataStatus.AWAITING_AUTHORISATION:
            return awaiting_authorisation()
        if self is ObReadConsentResponse1DataStatus.REJECTED:
            return rejected()
        if self is ObReadConsentResponse1DataStatus.REVOKED:
            return revoked()
