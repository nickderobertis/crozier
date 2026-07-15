

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EcommerceCustomerAddressesItemType(str, enum.Enum):
    BILLING = "billing"
    SHIPPING = "shipping"
    OTHER = "other"

    def visit(
        self,
        billing: typing.Callable[[], T_Result],
        shipping: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EcommerceCustomerAddressesItemType.BILLING:
            return billing()
        if self is EcommerceCustomerAddressesItemType.SHIPPING:
            return shipping()
        if self is EcommerceCustomerAddressesItemType.OTHER:
            return other()
