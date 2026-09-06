

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DealerDbModelsVoucherType(enum.StrEnum):
    """
    The type of voucher. Commercial is the default if not specified.
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
        if self is DealerDbModelsVoucherType.COMMERCIAL:
            return commercial()
        if self is DealerDbModelsVoucherType.INTERNAL:
            return internal()
        if self is DealerDbModelsVoucherType.TEMPORARY:
            return temporary()
        if self is DealerDbModelsVoucherType.RIGHT_TO_REPAIR:
            return right_to_repair()
