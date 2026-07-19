

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AmPolicyReqTrigger(enum.StrEnum):
    LOCATION_CHANGE = "LOCATION_CHANGE"
    PRA_CHANGE = "PRA_CHANGE"
    SARI_CHANGE = "SARI_CHANGE"
    RFSP_INDEX_CHANGE = "RFSP_INDEX_CHANGE"

    def visit(
        self,
        location_change: typing.Callable[[], T_Result],
        pra_change: typing.Callable[[], T_Result],
        sari_change: typing.Callable[[], T_Result],
        rfsp_index_change: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AmPolicyReqTrigger.LOCATION_CHANGE:
            return location_change()
        if self is AmPolicyReqTrigger.PRA_CHANGE:
            return pra_change()
        if self is AmPolicyReqTrigger.SARI_CHANGE:
            return sari_change()
        if self is AmPolicyReqTrigger.RFSP_INDEX_CHANGE:
            return rfsp_index_change()
