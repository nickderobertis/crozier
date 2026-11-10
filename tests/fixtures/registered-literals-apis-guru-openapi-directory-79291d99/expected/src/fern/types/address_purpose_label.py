

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AddressPurposeLabel(enum.StrEnum):
    """
    Field describing whether the associated address is being used for commercial or residential purposes.

    Note: This value will be `no_data` when Plaid does not have sufficient data to determine the address's use.
    """

    RESIDENTIAL = "residential"
    COMMERCIAL = "commercial"
    NO_DATA = "no_data"

    def visit(
        self,
        residential: typing.Callable[[], T_Result],
        commercial: typing.Callable[[], T_Result],
        no_data: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AddressPurposeLabel.RESIDENTIAL:
            return residential()
        if self is AddressPurposeLabel.COMMERCIAL:
            return commercial()
        if self is AddressPurposeLabel.NO_DATA:
            return no_data()
