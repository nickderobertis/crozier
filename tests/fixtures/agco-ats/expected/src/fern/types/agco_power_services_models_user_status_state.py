

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AgcoPowerServicesModelsUserStatusState(enum.StrEnum):
    """
    The state of the voucher
    """

    ACTIVE = "Active"
    INACTIVE = "Inactive"
    NONE = "None"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        inactive: typing.Callable[[], T_Result],
        none: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AgcoPowerServicesModelsUserStatusState.ACTIVE:
            return active()
        if self is AgcoPowerServicesModelsUserStatusState.INACTIVE:
            return inactive()
        if self is AgcoPowerServicesModelsUserStatusState.NONE:
            return none()
