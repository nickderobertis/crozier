

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MetadataMaintenanceOutcome(enum.StrEnum):
    """
    Whether metadata maintenance left work due for a namespace.
    """

    CAUGHT_UP = "caught_up"
    DUE = "due"

    def visit(self, caught_up: typing.Callable[[], T_Result], due: typing.Callable[[], T_Result]) -> T_Result:
        if self is MetadataMaintenanceOutcome.CAUGHT_UP:
            return caught_up()
        if self is MetadataMaintenanceOutcome.DUE:
            return due()
