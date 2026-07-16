

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObbcaData1OtherFeesChargesItemTariffType(str, enum.Enum):
    """
    TariffType which defines the fee and charges.
    """

    ELECTRONIC = "Electronic"
    MIXED = "Mixed"
    OTHER = "Other"

    def visit(
        self,
        electronic: typing.Callable[[], T_Result],
        mixed: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObbcaData1OtherFeesChargesItemTariffType.ELECTRONIC:
            return electronic()
        if self is ObbcaData1OtherFeesChargesItemTariffType.MIXED:
            return mixed()
        if self is ObbcaData1OtherFeesChargesItemTariffType.OTHER:
            return other()
