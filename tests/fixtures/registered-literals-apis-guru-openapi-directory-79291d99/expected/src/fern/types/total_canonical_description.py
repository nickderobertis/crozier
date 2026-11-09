

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TotalCanonicalDescription(enum.StrEnum):
    """
    Commonly used term to describe the line item.
    """

    BONUS = "BONUS"
    COMMISSION = "COMMISSION"
    OVERTIME = "OVERTIME"
    PAID_TIME_OFF = "PAID TIME OFF"
    REGULAR_PAY = "REGULAR PAY"
    VACATION = "VACATION"
    EMPLOYEE_MEDICARE = "EMPLOYEE MEDICARE"
    FICA = "FICA"
    SOCIAL_SECURITY_EMPLOYEE_TAX = "SOCIAL SECURITY EMPLOYEE TAX"
    MEDICAL = "MEDICAL"
    VISION = "VISION"
    DENTAL = "DENTAL"
    NET_PAY = "NET PAY"
    TAXES = "TAXES"
    NOT_FOUND = "NOT_FOUND"
    OTHER = "OTHER"

    def visit(
        self,
        bonus: typing.Callable[[], T_Result],
        commission: typing.Callable[[], T_Result],
        overtime: typing.Callable[[], T_Result],
        paid_time_off: typing.Callable[[], T_Result],
        regular_pay: typing.Callable[[], T_Result],
        vacation: typing.Callable[[], T_Result],
        employee_medicare: typing.Callable[[], T_Result],
        fica: typing.Callable[[], T_Result],
        social_security_employee_tax: typing.Callable[[], T_Result],
        medical: typing.Callable[[], T_Result],
        vision: typing.Callable[[], T_Result],
        dental: typing.Callable[[], T_Result],
        net_pay: typing.Callable[[], T_Result],
        taxes: typing.Callable[[], T_Result],
        not_found: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TotalCanonicalDescription.BONUS:
            return bonus()
        if self is TotalCanonicalDescription.COMMISSION:
            return commission()
        if self is TotalCanonicalDescription.OVERTIME:
            return overtime()
        if self is TotalCanonicalDescription.PAID_TIME_OFF:
            return paid_time_off()
        if self is TotalCanonicalDescription.REGULAR_PAY:
            return regular_pay()
        if self is TotalCanonicalDescription.VACATION:
            return vacation()
        if self is TotalCanonicalDescription.EMPLOYEE_MEDICARE:
            return employee_medicare()
        if self is TotalCanonicalDescription.FICA:
            return fica()
        if self is TotalCanonicalDescription.SOCIAL_SECURITY_EMPLOYEE_TAX:
            return social_security_employee_tax()
        if self is TotalCanonicalDescription.MEDICAL:
            return medical()
        if self is TotalCanonicalDescription.VISION:
            return vision()
        if self is TotalCanonicalDescription.DENTAL:
            return dental()
        if self is TotalCanonicalDescription.NET_PAY:
            return net_pay()
        if self is TotalCanonicalDescription.TAXES:
            return taxes()
        if self is TotalCanonicalDescription.NOT_FOUND:
            return not_found()
        if self is TotalCanonicalDescription.OTHER:
            return other()
