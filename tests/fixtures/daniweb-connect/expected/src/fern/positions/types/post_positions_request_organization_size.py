

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostPositionsRequestOrganizationSize(enum.StrEnum):
    SELF_EMPLOYED = "Self-employed"
    TWO9EMPLOYEES = "2 - 9 Employees"
    TEN49EMPLOYEES = "10 - 49 Employees"
    FIFTY99EMPLOYEES = "50 - 99 Employees"
    ONE_HUNDRED499EMPLOYEES = "100 - 499 Employees"
    FIVE_HUNDRED999EMPLOYEES = "500 - 999 Employees"
    ONE_THOUSAND4999EMPLOYEES = "1000 - 4999 Employees"
    FIVE_THOUSAND_EMPLOYEES = "5000+ Employees"
    DONT_KNOW = "Don't Know"

    def visit(
        self,
        self_employed: typing.Callable[[], T_Result],
        two9employees: typing.Callable[[], T_Result],
        ten49employees: typing.Callable[[], T_Result],
        fifty99employees: typing.Callable[[], T_Result],
        one_hundred499employees: typing.Callable[[], T_Result],
        five_hundred999employees: typing.Callable[[], T_Result],
        one_thousand4999employees: typing.Callable[[], T_Result],
        five_thousand_employees: typing.Callable[[], T_Result],
        dont_know: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostPositionsRequestOrganizationSize.SELF_EMPLOYED:
            return self_employed()
        if self is PostPositionsRequestOrganizationSize.TWO9EMPLOYEES:
            return two9employees()
        if self is PostPositionsRequestOrganizationSize.TEN49EMPLOYEES:
            return ten49employees()
        if self is PostPositionsRequestOrganizationSize.FIFTY99EMPLOYEES:
            return fifty99employees()
        if self is PostPositionsRequestOrganizationSize.ONE_HUNDRED499EMPLOYEES:
            return one_hundred499employees()
        if self is PostPositionsRequestOrganizationSize.FIVE_HUNDRED999EMPLOYEES:
            return five_hundred999employees()
        if self is PostPositionsRequestOrganizationSize.ONE_THOUSAND4999EMPLOYEES:
            return one_thousand4999employees()
        if self is PostPositionsRequestOrganizationSize.FIVE_THOUSAND_EMPLOYEES:
            return five_thousand_employees()
        if self is PostPositionsRequestOrganizationSize.DONT_KNOW:
            return dont_know()
