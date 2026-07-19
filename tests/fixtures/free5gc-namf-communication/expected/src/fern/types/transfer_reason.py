

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransferReason(enum.StrEnum):
    INIT_REG = "INIT_REG"
    MOBI_REG = "MOBI_REG"
    MOBI_REG_UE_VALIDATED = "MOBI_REG_UE_VALIDATED"

    def visit(
        self,
        init_reg: typing.Callable[[], T_Result],
        mobi_reg: typing.Callable[[], T_Result],
        mobi_reg_ue_validated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TransferReason.INIT_REG:
            return init_reg()
        if self is TransferReason.MOBI_REG:
            return mobi_reg()
        if self is TransferReason.MOBI_REG_UE_VALIDATED:
            return mobi_reg_ue_validated()
