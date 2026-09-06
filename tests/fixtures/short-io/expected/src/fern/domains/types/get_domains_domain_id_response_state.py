

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetDomainsDomainIdResponseState(enum.StrEnum):
    EXTRA_RECORDS = "extra_records"
    NOT_REGISTERED = "not_registered"
    CONFIGURED = "configured"
    NOT_CONFIGURED = "not_configured"
    REGISTRATION_PENDING = "registration_pending"
    NOT_VERIFIED = "not_verified"

    def visit(
        self,
        extra_records: typing.Callable[[], T_Result],
        not_registered: typing.Callable[[], T_Result],
        configured: typing.Callable[[], T_Result],
        not_configured: typing.Callable[[], T_Result],
        registration_pending: typing.Callable[[], T_Result],
        not_verified: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetDomainsDomainIdResponseState.EXTRA_RECORDS:
            return extra_records()
        if self is GetDomainsDomainIdResponseState.NOT_REGISTERED:
            return not_registered()
        if self is GetDomainsDomainIdResponseState.CONFIGURED:
            return configured()
        if self is GetDomainsDomainIdResponseState.NOT_CONFIGURED:
            return not_configured()
        if self is GetDomainsDomainIdResponseState.REGISTRATION_PENDING:
            return registration_pending()
        if self is GetDomainsDomainIdResponseState.NOT_VERIFIED:
            return not_verified()
