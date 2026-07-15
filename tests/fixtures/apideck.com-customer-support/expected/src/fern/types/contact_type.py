

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ContactType(str, enum.Enum):
    CUSTOMER = "customer"
    SUPPLIER = "supplier"
    EMPLOYEE = "employee"
    PERSONAL = "personal"

    def visit(
        self,
        customer: typing.Callable[[], T_Result],
        supplier: typing.Callable[[], T_Result],
        employee: typing.Callable[[], T_Result],
        personal: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ContactType.CUSTOMER:
            return customer()
        if self is ContactType.SUPPLIER:
            return supplier()
        if self is ContactType.EMPLOYEE:
            return employee()
        if self is ContactType.PERSONAL:
            return personal()
