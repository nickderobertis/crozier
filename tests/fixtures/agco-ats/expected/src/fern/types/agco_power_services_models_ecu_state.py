

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AgcoPowerServicesModelsEcuState(enum.StrEnum):
    """
    The state of the ECU
    """

    ACTIVE = "Active"
    INACTIVE = "Inactive"
    DAMAGED = "Damaged"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        inactive: typing.Callable[[], T_Result],
        damaged: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AgcoPowerServicesModelsEcuState.ACTIVE:
            return active()
        if self is AgcoPowerServicesModelsEcuState.INACTIVE:
            return inactive()
        if self is AgcoPowerServicesModelsEcuState.DAMAGED:
            return damaged()
