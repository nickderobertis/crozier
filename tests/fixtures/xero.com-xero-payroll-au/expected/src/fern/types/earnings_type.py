

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EarningsType(str, enum.Enum):
    FIXED = "FIXED"
    ORDINARYTIMEEARNINGS = "ORDINARYTIMEEARNINGS"
    OVERTIMEEARNINGS = "OVERTIMEEARNINGS"
    ALLOWANCE = "ALLOWANCE"
    LUMPSUMD = "LUMPSUMD"
    EMPLOYMENTTERMINATIONPAYMENT = "EMPLOYMENTTERMINATIONPAYMENT"
    LUMPSUMA = "LUMPSUMA"
    LUMPSUMB = "LUMPSUMB"
    BONUSESANDCOMMISSIONS = "BONUSESANDCOMMISSIONS"
    LUMPSUME = "LUMPSUME"

    def visit(
        self,
        fixed: typing.Callable[[], T_Result],
        ordinarytimeearnings: typing.Callable[[], T_Result],
        overtimeearnings: typing.Callable[[], T_Result],
        allowance: typing.Callable[[], T_Result],
        lumpsumd: typing.Callable[[], T_Result],
        employmentterminationpayment: typing.Callable[[], T_Result],
        lumpsuma: typing.Callable[[], T_Result],
        lumpsumb: typing.Callable[[], T_Result],
        bonusesandcommissions: typing.Callable[[], T_Result],
        lumpsume: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EarningsType.FIXED:
            return fixed()
        if self is EarningsType.ORDINARYTIMEEARNINGS:
            return ordinarytimeearnings()
        if self is EarningsType.OVERTIMEEARNINGS:
            return overtimeearnings()
        if self is EarningsType.ALLOWANCE:
            return allowance()
        if self is EarningsType.LUMPSUMD:
            return lumpsumd()
        if self is EarningsType.EMPLOYMENTTERMINATIONPAYMENT:
            return employmentterminationpayment()
        if self is EarningsType.LUMPSUMA:
            return lumpsuma()
        if self is EarningsType.LUMPSUMB:
            return lumpsumb()
        if self is EarningsType.BONUSESANDCOMMISSIONS:
            return bonusesandcommissions()
        if self is EarningsType.LUMPSUME:
            return lumpsume()
