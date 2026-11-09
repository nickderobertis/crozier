

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CaseSourceDataStatus(enum.StrEnum):
    """
    The status of source data of case. If the value of sourceDataStatus is SOURCE_DEPRECATED then it means that the Case has been migrated from old court site to a new court site and the data being shown in the API response is from a old court site. If the sourceDataStatus is NO_LONGER_AVAILABLE_IN_COURT then it means that a particular case is invalid in the court site.
    """

    NO_LONGER_AVAILABLE_IN_COURT = "NO_LONGER_AVAILABLE_IN_COURT"
    SOURCE_DEPRECATED = "SOURCE_DEPRECATED"

    def visit(
        self,
        no_longer_available_in_court: typing.Callable[[], T_Result],
        source_deprecated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CaseSourceDataStatus.NO_LONGER_AVAILABLE_IN_COURT:
            return no_longer_available_in_court()
        if self is CaseSourceDataStatus.SOURCE_DEPRECATED:
            return source_deprecated()
