

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CustomerSupportCustomerStatus(str, enum.Enum):
    """
    Customer status
    """

    ACTIVE = "active"
    ARCHIVED = "archived"
    GDPR_ERASURE_REQUEST = "gdpr-erasure-request"
    UNKNOWN = "unknown"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        archived: typing.Callable[[], T_Result],
        gdpr_erasure_request: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CustomerSupportCustomerStatus.ACTIVE:
            return active()
        if self is CustomerSupportCustomerStatus.ARCHIVED:
            return archived()
        if self is CustomerSupportCustomerStatus.GDPR_ERASURE_REQUEST:
            return gdpr_erasure_request()
        if self is CustomerSupportCustomerStatus.UNKNOWN:
            return unknown()
