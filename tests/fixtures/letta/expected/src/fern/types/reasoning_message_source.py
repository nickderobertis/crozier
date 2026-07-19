

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReasoningMessageSource(enum.StrEnum):
    REASONER_MODEL = "reasoner_model"
    NON_REASONER_MODEL = "non_reasoner_model"

    def visit(
        self, reasoner_model: typing.Callable[[], T_Result], non_reasoner_model: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is ReasoningMessageSource.REASONER_MODEL:
            return reasoner_model()
        if self is ReasoningMessageSource.NON_REASONER_MODEL:
            return non_reasoner_model()
