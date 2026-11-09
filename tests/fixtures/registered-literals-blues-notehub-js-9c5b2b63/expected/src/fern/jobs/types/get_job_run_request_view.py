

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetJobRunRequestView(enum.StrEnum):
    SUMMARY = "summary"
    DETAIL = "detail"

    def visit(self, summary: typing.Callable[[], T_Result], detail: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetJobRunRequestView.SUMMARY:
            return summary()
        if self is GetJobRunRequestView.DETAIL:
            return detail()
