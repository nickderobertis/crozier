

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BarRecordStatus(enum.StrEnum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"
    NOT_CLASSIFIED = "Not Classified"
    UNKNOWN = "Unknown"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        inactive: typing.Callable[[], T_Result],
        not_classified: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BarRecordStatus.ACTIVE:
            return active()
        if self is BarRecordStatus.INACTIVE:
            return inactive()
        if self is BarRecordStatus.NOT_CLASSIFIED:
            return not_classified()
        if self is BarRecordStatus.UNKNOWN:
            return unknown()
