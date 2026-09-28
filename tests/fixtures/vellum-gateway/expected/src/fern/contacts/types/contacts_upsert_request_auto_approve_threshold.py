

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ContactsUpsertRequestAutoApproveThreshold(enum.StrEnum):
    NONE = "none"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        low: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        high: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ContactsUpsertRequestAutoApproveThreshold.NONE:
            return none()
        if self is ContactsUpsertRequestAutoApproveThreshold.LOW:
            return low()
        if self is ContactsUpsertRequestAutoApproveThreshold.MEDIUM:
            return medium()
        if self is ContactsUpsertRequestAutoApproveThreshold.HIGH:
            return high()
