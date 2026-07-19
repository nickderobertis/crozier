

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class MetadataSendFeedbackRequestFeature(enum.StrEnum):
    LETTA_CODE = "letta-code"
    SDK = "sdk"

    def visit(self, letta_code: typing.Callable[[], T_Result], sdk: typing.Callable[[], T_Result]) -> T_Result:
        if self is MetadataSendFeedbackRequestFeature.LETTA_CODE:
            return letta_code()
        if self is MetadataSendFeedbackRequestFeature.SDK:
            return sdk()
