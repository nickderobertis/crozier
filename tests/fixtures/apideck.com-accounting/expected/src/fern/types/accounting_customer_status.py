

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AccountingCustomerStatus(enum.StrEnum):
    """
    Customer status
    """

    ACTIVE = "active"
    INACTIVE = "inactive"
    ARCHIVED = "archived"
    GDPR_ERASURE_REQUEST = "gdpr-erasure-request"
    UNKNOWN = "unknown"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        inactive: typing.Callable[[], T_Result],
        archived: typing.Callable[[], T_Result],
        gdpr_erasure_request: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AccountingCustomerStatus.ACTIVE:
            return active()
        if self is AccountingCustomerStatus.INACTIVE:
            return inactive()
        if self is AccountingCustomerStatus.ARCHIVED:
            return archived()
        if self is AccountingCustomerStatus.GDPR_ERASURE_REQUEST:
            return gdpr_erasure_request()
        if self is AccountingCustomerStatus.UNKNOWN:
            return unknown()
