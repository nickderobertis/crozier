

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreateNonDraftJobJobType(enum.StrEnum):
    QUOTE = "Quote"
    ESTIMATE = "Estimate"
    CHARGE_UP = "Charge Up"

    def visit(
        self,
        quote: typing.Callable[[], T_Result],
        estimate: typing.Callable[[], T_Result],
        charge_up: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateNonDraftJobJobType.QUOTE:
            return quote()
        if self is CreateNonDraftJobJobType.ESTIMATE:
            return estimate()
        if self is CreateNonDraftJobJobType.CHARGE_UP:
            return charge_up()
