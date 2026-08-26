

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FuelType(enum.StrEnum):
    """
    The vehicle's fuel type
    """

    ELECTRIC = "electric"
    DIESEL = "diesel"
    HYDROGEN = "hydrogen"
    LIQUEFIED_PETROLEUM_GAS = "liquefied_petroleum_gas"
    COMPRESSED_NATURAL_GAS = "compressed_natural_gas"
    LIQUEFIED_NATURAL_GAS = "liquefied_natural_gas"
    ETHANOL = "ethanol"
    PETROL = "petrol"

    def visit(
        self,
        electric: typing.Callable[[], T_Result],
        diesel: typing.Callable[[], T_Result],
        hydrogen: typing.Callable[[], T_Result],
        liquefied_petroleum_gas: typing.Callable[[], T_Result],
        compressed_natural_gas: typing.Callable[[], T_Result],
        liquefied_natural_gas: typing.Callable[[], T_Result],
        ethanol: typing.Callable[[], T_Result],
        petrol: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FuelType.ELECTRIC:
            return electric()
        if self is FuelType.DIESEL:
            return diesel()
        if self is FuelType.HYDROGEN:
            return hydrogen()
        if self is FuelType.LIQUEFIED_PETROLEUM_GAS:
            return liquefied_petroleum_gas()
        if self is FuelType.COMPRESSED_NATURAL_GAS:
            return compressed_natural_gas()
        if self is FuelType.LIQUEFIED_NATURAL_GAS:
            return liquefied_natural_gas()
        if self is FuelType.ETHANOL:
            return ethanol()
        if self is FuelType.PETROL:
            return petrol()
