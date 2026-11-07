

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IndexMode(enum.StrEnum):
    """
    Wallet index mode that determines how chain data is tracked.
    """

    PERSONAL = "personal"
    FULL = "full"
    NONE = "none"

    def visit(
        self,
        personal: typing.Callable[[], T_Result],
        full: typing.Callable[[], T_Result],
        none: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IndexMode.PERSONAL:
            return personal()
        if self is IndexMode.FULL:
            return full()
        if self is IndexMode.NONE:
            return none()
