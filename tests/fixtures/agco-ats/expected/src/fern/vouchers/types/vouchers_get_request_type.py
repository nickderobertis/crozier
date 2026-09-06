

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class VouchersGetRequestType(enum.StrEnum):
    COMMERCIAL = "Commercial"
    INTERNAL = "Internal"
    TEMPORARY = "Temporary"
    RIGHT_TO_REPAIR = "RightToRepair"

    def visit(
        self,
        commercial: typing.Callable[[], T_Result],
        internal: typing.Callable[[], T_Result],
        temporary: typing.Callable[[], T_Result],
        right_to_repair: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VouchersGetRequestType.COMMERCIAL:
            return commercial()
        if self is VouchersGetRequestType.INTERNAL:
            return internal()
        if self is VouchersGetRequestType.TEMPORARY:
            return temporary()
        if self is VouchersGetRequestType.RIGHT_TO_REPAIR:
            return right_to_repair()
