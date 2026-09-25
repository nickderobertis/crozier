

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetJobsRequestFilterJobType(enum.StrEnum):
    QUOTE = "Quote"
    ESTIMATE = "Estimate"
    CHARGE_UP = "Charge Up"

    def visit(
        self,
        quote: typing.Callable[[], T_Result],
        estimate: typing.Callable[[], T_Result],
        charge_up: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetJobsRequestFilterJobType.QUOTE:
            return quote()
        if self is GetJobsRequestFilterJobType.ESTIMATE:
            return estimate()
        if self is GetJobsRequestFilterJobType.CHARGE_UP:
            return charge_up()
