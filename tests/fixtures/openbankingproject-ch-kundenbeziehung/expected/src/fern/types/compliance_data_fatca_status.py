

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ComplianceDataFatcaStatus(enum.StrEnum):
    US_PERSON = "us_person"
    NON_US_PERSON = "non_us_person"
    UNCERTAIN = "uncertain"

    def visit(
        self,
        us_person: typing.Callable[[], T_Result],
        non_us_person: typing.Callable[[], T_Result],
        uncertain: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ComplianceDataFatcaStatus.US_PERSON:
            return us_person()
        if self is ComplianceDataFatcaStatus.NON_US_PERSON:
            return non_us_person()
        if self is ComplianceDataFatcaStatus.UNCERTAIN:
            return uncertain()
