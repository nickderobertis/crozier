

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JobEmploymentTerms(enum.StrEnum):
    FULL_TIME = "full-time"
    PART_TIME = "part-time"
    INTERNSHIP = "internship"
    CONTRACTOR = "contractor"
    EMPLOYEE = "employee"
    FREELANCE = "freelance"
    TEMP = "temp"
    SEASONAL = "seasonal"
    VOLUNTEER = "volunteer"
    OTHER = "other"

    def visit(
        self,
        full_time: typing.Callable[[], T_Result],
        part_time: typing.Callable[[], T_Result],
        internship: typing.Callable[[], T_Result],
        contractor: typing.Callable[[], T_Result],
        employee: typing.Callable[[], T_Result],
        freelance: typing.Callable[[], T_Result],
        temp: typing.Callable[[], T_Result],
        seasonal: typing.Callable[[], T_Result],
        volunteer: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is JobEmploymentTerms.FULL_TIME:
            return full_time()
        if self is JobEmploymentTerms.PART_TIME:
            return part_time()
        if self is JobEmploymentTerms.INTERNSHIP:
            return internship()
        if self is JobEmploymentTerms.CONTRACTOR:
            return contractor()
        if self is JobEmploymentTerms.EMPLOYEE:
            return employee()
        if self is JobEmploymentTerms.FREELANCE:
            return freelance()
        if self is JobEmploymentTerms.TEMP:
            return temp()
        if self is JobEmploymentTerms.SEASONAL:
            return seasonal()
        if self is JobEmploymentTerms.VOLUNTEER:
            return volunteer()
        if self is JobEmploymentTerms.OTHER:
            return other()
