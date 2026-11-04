

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CapabilityAccountRequirementRetentionModesItem(enum.StrEnum):
    TEMPORARY = "temporary"
    SAVED = "saved"

    def visit(self, temporary: typing.Callable[[], T_Result], saved: typing.Callable[[], T_Result]) -> T_Result:
        if self is CapabilityAccountRequirementRetentionModesItem.TEMPORARY:
            return temporary()
        if self is CapabilityAccountRequirementRetentionModesItem.SAVED:
            return saved()
