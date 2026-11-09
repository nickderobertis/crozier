

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetCaseHearingsRequestSortBy(enum.StrEnum):
    LATEST_TO_OLDEST = "latest to oldest"
    OLDEST_TO_LATEST = "oldest to latest"

    def visit(
        self, latest_to_oldest: typing.Callable[[], T_Result], oldest_to_latest: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is GetCaseHearingsRequestSortBy.LATEST_TO_OLDEST:
            return latest_to_oldest()
        if self is GetCaseHearingsRequestSortBy.OLDEST_TO_LATEST:
            return oldest_to_latest()
