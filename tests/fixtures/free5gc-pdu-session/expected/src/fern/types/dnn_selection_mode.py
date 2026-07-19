

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DnnSelectionMode(enum.StrEnum):
    VERIFIED = "VERIFIED"
    UE_DNN_NOT_VERIFIED = "UE_DNN_NOT_VERIFIED"
    NW_DNN_NOT_VERIFIED = "NW_DNN_NOT_VERIFIED"

    def visit(
        self,
        verified: typing.Callable[[], T_Result],
        ue_dnn_not_verified: typing.Callable[[], T_Result],
        nw_dnn_not_verified: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DnnSelectionMode.VERIFIED:
            return verified()
        if self is DnnSelectionMode.UE_DNN_NOT_VERIFIED:
            return ue_dnn_not_verified()
        if self is DnnSelectionMode.NW_DNN_NOT_VERIFIED:
            return nw_dnn_not_verified()
