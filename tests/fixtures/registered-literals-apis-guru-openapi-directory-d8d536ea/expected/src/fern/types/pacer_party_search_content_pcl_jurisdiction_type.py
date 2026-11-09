

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PacerPartySearchContentPclJurisdictionType(enum.StrEnum):
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
        if self is PacerPartySearchContentPclJurisdictionType.APPELLATE:
            return appellate()
        if self is PacerPartySearchContentPclJurisdictionType.BANKRUPTCY:
            return bankruptcy()
        if self is PacerPartySearchContentPclJurisdictionType.CRIMINAL:
            return criminal()
        if self is PacerPartySearchContentPclJurisdictionType.CIVIL:
            return civil()
        if self is PacerPartySearchContentPclJurisdictionType.MULTI_DISTRICT_LITIGATION:
            return multi_district_litigation()
