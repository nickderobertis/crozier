

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class SupplierStatus(str, enum.Enum):
    """
    Supplier status
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
        if self is SupplierStatus.ACTIVE:
            return active()
        if self is SupplierStatus.INACTIVE:
            return inactive()
        if self is SupplierStatus.ARCHIVED:
            return archived()
        if self is SupplierStatus.GDPR_ERASURE_REQUEST:
            return gdpr_erasure_request()
        if self is SupplierStatus.UNKNOWN:
            return unknown()
