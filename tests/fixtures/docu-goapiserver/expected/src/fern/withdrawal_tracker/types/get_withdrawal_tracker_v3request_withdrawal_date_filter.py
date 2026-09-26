

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetWithdrawalTrackerV3RequestWithdrawalDateFilter(enum.StrEnum):
    EMS_ENTRY = "ems_entry"
    PROCARE = "procare"
    ESTIMATED = "estimated"

    def visit(
        self,
        ems_entry: typing.Callable[[], T_Result],
        procare: typing.Callable[[], T_Result],
        estimated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetWithdrawalTrackerV3RequestWithdrawalDateFilter.EMS_ENTRY:
            return ems_entry()
        if self is GetWithdrawalTrackerV3RequestWithdrawalDateFilter.PROCARE:
            return procare()
        if self is GetWithdrawalTrackerV3RequestWithdrawalDateFilter.ESTIMATED:
            return estimated()
