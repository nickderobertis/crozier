

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VlanStatusLabel(enum.StrEnum):
    ACTIVE = "Active"
    RESERVED = "Reserved"
    DEPRECATED = "Deprecated"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        reserved: typing.Callable[[], T_Result],
        deprecated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VlanStatusLabel.ACTIVE:
            return active()
        if self is VlanStatusLabel.RESERVED:
            return reserved()
        if self is VlanStatusLabel.DEPRECATED:
            return deprecated()
