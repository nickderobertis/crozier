

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NormJudgePublicDataJudicialSourceType(enum.StrEnum):
    """
    Type of acquisition of the data source
    """

    WEBSITE = "Website"
    OTHER = "Other"

    def visit(self, website: typing.Callable[[], T_Result], other: typing.Callable[[], T_Result]) -> T_Result:
        if self is NormJudgePublicDataJudicialSourceType.WEBSITE:
            return website()
        if self is NormJudgePublicDataJudicialSourceType.OTHER:
            return other()
