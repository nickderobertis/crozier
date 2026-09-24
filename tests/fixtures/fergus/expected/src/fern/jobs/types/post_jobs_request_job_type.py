

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostJobsRequestJobType(enum.StrEnum):
    QUOTE = "Quote"
    ESTIMATE = "Estimate"
    CHARGE_UP = "Charge Up"

    def visit(
        self,
        quote: typing.Callable[[], T_Result],
        estimate: typing.Callable[[], T_Result],
        charge_up: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostJobsRequestJobType.QUOTE:
            return quote()
        if self is PostJobsRequestJobType.ESTIMATE:
            return estimate()
        if self is PostJobsRequestJobType.CHARGE_UP:
            return charge_up()
