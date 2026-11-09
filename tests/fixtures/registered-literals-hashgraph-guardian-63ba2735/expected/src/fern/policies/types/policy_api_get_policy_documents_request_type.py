

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PolicyApiGetPolicyDocumentsRequestType(enum.StrEnum):
    VC = "VC"
    VP = "VP"

    def visit(self, vc: typing.Callable[[], T_Result], vp: typing.Callable[[], T_Result]) -> T_Result:
        if self is PolicyApiGetPolicyDocumentsRequestType.VC:
            return vc()
        if self is PolicyApiGetPolicyDocumentsRequestType.VP:
            return vp()
