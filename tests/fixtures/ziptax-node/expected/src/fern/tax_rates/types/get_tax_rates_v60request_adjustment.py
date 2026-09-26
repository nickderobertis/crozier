

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetTaxRatesV60RequestAdjustment(enum.StrEnum):
    """
    Sourcing/unincorporated-area handling. Defaults to 'auto', which applies the appropriate sourcing adjustment on geo (address) lookups in unincorporated areas. The values 'origin' and 'destination' are accepted but currently do not change the resolved result.
    """

    AUTO = "auto"
    ORIGIN = "origin"
    DESTINATION = "destination"

    def visit(
        self,
        auto: typing.Callable[[], T_Result],
        origin: typing.Callable[[], T_Result],
        destination: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetTaxRatesV60RequestAdjustment.AUTO:
            return auto()
        if self is GetTaxRatesV60RequestAdjustment.ORIGIN:
            return origin()
        if self is GetTaxRatesV60RequestAdjustment.DESTINATION:
            return destination()
