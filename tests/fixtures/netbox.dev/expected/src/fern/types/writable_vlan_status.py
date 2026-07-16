

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WritableVlanStatus(enum.StrEnum):
    ACTIVE = "active"
    RESERVED = "reserved"
    DEPRECATED = "deprecated"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        reserved: typing.Callable[[], T_Result],
        deprecated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WritableVlanStatus.ACTIVE:
            return active()
        if self is WritableVlanStatus.RESERVED:
            return reserved()
        if self is WritableVlanStatus.DEPRECATED:
            return deprecated()
