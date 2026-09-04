

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AddressAddressType(enum.StrEnum):
    RESIDENTIAL = "residential"
    MAILING = "mailing"
    BUSINESS = "business"
    TEMPORARY = "temporary"

    def visit(
        self,
        residential: typing.Callable[[], T_Result],
        mailing: typing.Callable[[], T_Result],
        business: typing.Callable[[], T_Result],
        temporary: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AddressAddressType.RESIDENTIAL:
            return residential()
        if self is AddressAddressType.MAILING:
            return mailing()
        if self is AddressAddressType.BUSINESS:
            return business()
        if self is AddressAddressType.TEMPORARY:
            return temporary()
