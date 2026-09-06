

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DealerDbModelsVoucherHistoryType(enum.StrEnum):
    """
    The type of voucher.
    """

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
        if self is DealerDbModelsVoucherHistoryType.COMMERCIAL:
            return commercial()
        if self is DealerDbModelsVoucherHistoryType.INTERNAL:
            return internal()
        if self is DealerDbModelsVoucherHistoryType.TEMPORARY:
            return temporary()
        if self is DealerDbModelsVoucherHistoryType.RIGHT_TO_REPAIR:
            return right_to_repair()
