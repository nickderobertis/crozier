

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActUpdateRequestReasonCodeReasonCode(enum.StrEnum):
    PROMPT_INJECTION = "PROMPT_INJECTION"
    UNAUTHORIZED_ACTION = "UNAUTHORIZED_ACTION"
    DATA_EXPOSURE = "DATA_EXPOSURE"
    DECEPTIVE_COMPLETION = "DECEPTIVE_COMPLETION"
    COST_ABUSE = "COST_ABUSE"
    OTHER = "OTHER"

    def visit(
        self,
        prompt_injection: typing.Callable[[], T_Result],
        unauthorized_action: typing.Callable[[], T_Result],
        data_exposure: typing.Callable[[], T_Result],
        deceptive_completion: typing.Callable[[], T_Result],
        cost_abuse: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ActUpdateRequestReasonCodeReasonCode.PROMPT_INJECTION:
            return prompt_injection()
        if self is ActUpdateRequestReasonCodeReasonCode.UNAUTHORIZED_ACTION:
            return unauthorized_action()
        if self is ActUpdateRequestReasonCodeReasonCode.DATA_EXPOSURE:
            return data_exposure()
        if self is ActUpdateRequestReasonCodeReasonCode.DECEPTIVE_COMPLETION:
            return deceptive_completion()
        if self is ActUpdateRequestReasonCodeReasonCode.COST_ABUSE:
            return cost_abuse()
        if self is ActUpdateRequestReasonCodeReasonCode.OTHER:
            return other()
