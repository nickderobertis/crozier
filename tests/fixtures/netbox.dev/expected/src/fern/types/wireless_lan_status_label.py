

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WirelessLanStatusLabel(enum.StrEnum):
    ACTIVE = "Active"
    RESERVED = "Reserved"
    DISABLED = "Disabled"
    DEPRECATED = "Deprecated"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        reserved: typing.Callable[[], T_Result],
        disabled: typing.Callable[[], T_Result],
        deprecated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WirelessLanStatusLabel.ACTIVE:
            return active()
        if self is WirelessLanStatusLabel.RESERVED:
            return reserved()
        if self is WirelessLanStatusLabel.DISABLED:
            return disabled()
        if self is WirelessLanStatusLabel.DEPRECATED:
            return deprecated()
