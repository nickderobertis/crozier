

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EnergyBaseSubType(enum.StrEnum):
    """
    Energy subtype. This field is not mandatory and therefore if it is not present, it means that the resource consumer should only process the primary energy type. The enumeration of the subtypes is not exhaustive and may contain more elements depending on the evolution of the vehicles. The consumer of the data must take this constraint into account. The Fossil and Electric energy subtypes are only used to populate this subtype for the default Fuel and Eletric types.
      * Electric and hydrogen vehicles energy types are considered as low emission energies whereas fuel(fossil) is associated to thermic energy
    """

    FOSSIL_ENERGY = "FossilEnergy"
    ELECTRIC_ENERGY = "ElectricEnergy"
    HYDROGEN = "Hydrogen"

    def visit(
        self,
        fossil_energy: typing.Callable[[], T_Result],
        electric_energy: typing.Callable[[], T_Result],
        hydrogen: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EnergyBaseSubType.FOSSIL_ENERGY:
            return fossil_energy()
        if self is EnergyBaseSubType.ELECTRIC_ENERGY:
            return electric_energy()
        if self is EnergyBaseSubType.HYDROGEN:
            return hydrogen()
