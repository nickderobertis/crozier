

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AddressType(str, enum.Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary"
    HOME = "home"
    OFFICE = "office"
    SHIPPING = "shipping"
    BILLING = "billing"
    OTHER = "other"

    def visit(
        self,
        primary: typing.Callable[[], T_Result],
        secondary: typing.Callable[[], T_Result],
        home: typing.Callable[[], T_Result],
        office: typing.Callable[[], T_Result],
        shipping: typing.Callable[[], T_Result],
        billing: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AddressType.PRIMARY:
            return primary()
        if self is AddressType.SECONDARY:
            return secondary()
        if self is AddressType.HOME:
            return home()
        if self is AddressType.OFFICE:
            return office()
        if self is AddressType.SHIPPING:
            return shipping()
        if self is AddressType.BILLING:
            return billing()
        if self is AddressType.OTHER:
            return other()
