

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HrisEventType(enum.StrEnum):
    ALL = "*"
    HRIS_EMPLOYEE_CREATED = "hris.employee.created"
    HRIS_EMPLOYEE_UPDATED = "hris.employee.updated"
    HRIS_EMPLOYEE_DELETED = "hris.employee.deleted"
    HRIS_COMPANY_CREATED = "hris.company.created"
    HRIS_COMPANY_UPDATED = "hris.company.updated"
    HRIS_COMPANY_DELETED = "hris.company.deleted"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        hris_employee_created: typing.Callable[[], T_Result],
        hris_employee_updated: typing.Callable[[], T_Result],
        hris_employee_deleted: typing.Callable[[], T_Result],
        hris_company_created: typing.Callable[[], T_Result],
        hris_company_updated: typing.Callable[[], T_Result],
        hris_company_deleted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is HrisEventType.ALL:
            return all_()
        if self is HrisEventType.HRIS_EMPLOYEE_CREATED:
            return hris_employee_created()
        if self is HrisEventType.HRIS_EMPLOYEE_UPDATED:
            return hris_employee_updated()
        if self is HrisEventType.HRIS_EMPLOYEE_DELETED:
            return hris_employee_deleted()
        if self is HrisEventType.HRIS_COMPANY_CREATED:
            return hris_company_created()
        if self is HrisEventType.HRIS_COMPANY_UPDATED:
            return hris_company_updated()
        if self is HrisEventType.HRIS_COMPANY_DELETED:
            return hris_company_deleted()
