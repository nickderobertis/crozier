

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EcommerceCustomerStatus(str, enum.Enum):
    """
    The current status of the customer
    """

    ACTIVE = "active"
    ARCHIVED = "archived"

    def visit(self, active: typing.Callable[[], T_Result], archived: typing.Callable[[], T_Result]) -> T_Result:
        if self is EcommerceCustomerStatus.ACTIVE:
            return active()
        if self is EcommerceCustomerStatus.ARCHIVED:
            return archived()
