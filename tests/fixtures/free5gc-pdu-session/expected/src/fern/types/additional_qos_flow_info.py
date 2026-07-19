

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AdditionalQosFlowInfo(enum.StrEnum):
    MORE_LIKELY = "MORE_LIKELY"

    def visit(self, more_likely: typing.Callable[[], T_Result]) -> T_Result:
        if self is AdditionalQosFlowInfo.MORE_LIKELY:
            return more_likely()
