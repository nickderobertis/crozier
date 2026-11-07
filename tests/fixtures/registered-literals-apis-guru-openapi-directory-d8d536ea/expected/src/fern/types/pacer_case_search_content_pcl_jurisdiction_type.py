

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PacerCaseSearchContentPclJurisdictionType(enum.StrEnum):
    """
    Link to case in the case management/electronic case files (CM/ECF) system at the court.
    """

    APPELLATE = "Appellate"
    BANKRUPTCY = "Bankruptcy"
    CRIMINAL = "Criminal"
    CIVIL = "Civil"
    MULTI_DISTRICT_LITIGATION = "Multi-district Litigation"

    def visit(
        self,
        appellate: typing.Callable[[], T_Result],
        bankruptcy: typing.Callable[[], T_Result],
        criminal: typing.Callable[[], T_Result],
        civil: typing.Callable[[], T_Result],
        multi_district_litigation: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PacerCaseSearchContentPclJurisdictionType.APPELLATE:
            return appellate()
        if self is PacerCaseSearchContentPclJurisdictionType.BANKRUPTCY:
            return bankruptcy()
        if self is PacerCaseSearchContentPclJurisdictionType.CRIMINAL:
            return criminal()
        if self is PacerCaseSearchContentPclJurisdictionType.CIVIL:
            return civil()
        if self is PacerCaseSearchContentPclJurisdictionType.MULTI_DISTRICT_LITIGATION:
            return multi_district_litigation()
