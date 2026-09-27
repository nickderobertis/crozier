

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetPaymentsV3RequestGroupBy(enum.StrEnum):
    SCHOOL_ID = "school_id"
    FAMILY_ID = "family_id"
    MONTH = "month"
    STATE = "state"
    PAYMENT_MODE = "payment_mode"
    PAYMENT_METHOD_SUB_KIND = "payment_method_sub_kind"

    def visit(
        self,
        school_id: typing.Callable[[], T_Result],
        family_id: typing.Callable[[], T_Result],
        month: typing.Callable[[], T_Result],
        state: typing.Callable[[], T_Result],
        payment_mode: typing.Callable[[], T_Result],
        payment_method_sub_kind: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetPaymentsV3RequestGroupBy.SCHOOL_ID:
            return school_id()
        if self is GetPaymentsV3RequestGroupBy.FAMILY_ID:
            return family_id()
        if self is GetPaymentsV3RequestGroupBy.MONTH:
            return month()
        if self is GetPaymentsV3RequestGroupBy.STATE:
            return state()
        if self is GetPaymentsV3RequestGroupBy.PAYMENT_MODE:
            return payment_mode()
        if self is GetPaymentsV3RequestGroupBy.PAYMENT_METHOD_SUB_KIND:
            return payment_method_sub_kind()
