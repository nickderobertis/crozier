

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetChainsChainIdStatusResponseJobsItemVerdict(enum.StrEnum):
    FRESH = "fresh"
    LATE = "late"
    FAILING = "failing"
    FILLING = "filling"
    STALLED = "stalled"
    NEVER = "never"

    def visit(
        self,
        fresh: typing.Callable[[], T_Result],
        late: typing.Callable[[], T_Result],
        failing: typing.Callable[[], T_Result],
        filling: typing.Callable[[], T_Result],
        stalled: typing.Callable[[], T_Result],
        never: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetChainsChainIdStatusResponseJobsItemVerdict.FRESH:
            return fresh()
        if self is GetChainsChainIdStatusResponseJobsItemVerdict.LATE:
            return late()
        if self is GetChainsChainIdStatusResponseJobsItemVerdict.FAILING:
            return failing()
        if self is GetChainsChainIdStatusResponseJobsItemVerdict.FILLING:
            return filling()
        if self is GetChainsChainIdStatusResponseJobsItemVerdict.STALLED:
            return stalled()
        if self is GetChainsChainIdStatusResponseJobsItemVerdict.NEVER:
            return never()
