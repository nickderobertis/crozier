

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AnchoreImageImageStatus(enum.StrEnum):
    """
    State of the image
    """

    ACTIVE = "active"
    INACTIVE = "inactive"
    DISABLED = "disabled"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        inactive: typing.Callable[[], T_Result],
        disabled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AnchoreImageImageStatus.ACTIVE:
            return active()
        if self is AnchoreImageImageStatus.INACTIVE:
            return inactive()
        if self is AnchoreImageImageStatus.DISABLED:
            return disabled()
