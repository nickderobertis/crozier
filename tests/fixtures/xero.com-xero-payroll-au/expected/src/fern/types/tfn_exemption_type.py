

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TfnExemptionType(enum.StrEnum):
    NOTQUOTED = "NOTQUOTED"
    PENDING = "PENDING"
    PENSIONER = "PENSIONER"
    UNDER18 = "UNDER18"

    def visit(
        self,
        notquoted: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
        pensioner: typing.Callable[[], T_Result],
        under18: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TfnExemptionType.NOTQUOTED:
            return notquoted()
        if self is TfnExemptionType.PENDING:
            return pending()
        if self is TfnExemptionType.PENSIONER:
            return pensioner()
        if self is TfnExemptionType.UNDER18:
            return under18()
