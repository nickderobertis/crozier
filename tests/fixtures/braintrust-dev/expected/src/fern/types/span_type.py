

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SpanType(enum.StrEnum):
    """
    Type of the span, for display purposes only
    """

    LLM = "llm"
    SCORE = "score"
    FUNCTION = "function"
    EVAL = "eval"
    TASK = "task"
    TOOL = "tool"
    AUTOMATION = "automation"
    FACET = "facet"
    PREPROCESSOR = "preprocessor"
    CLASSIFIER = "classifier"
    REVIEW = "review"

    def visit(
        self,
        llm: typing.Callable[[], T_Result],
        score: typing.Callable[[], T_Result],
        function: typing.Callable[[], T_Result],
        eval: typing.Callable[[], T_Result],
        task: typing.Callable[[], T_Result],
        tool: typing.Callable[[], T_Result],
        automation: typing.Callable[[], T_Result],
        facet: typing.Callable[[], T_Result],
        preprocessor: typing.Callable[[], T_Result],
        classifier: typing.Callable[[], T_Result],
        review: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SpanType.LLM:
            return llm()
        if self is SpanType.SCORE:
            return score()
        if self is SpanType.FUNCTION:
            return function()
        if self is SpanType.EVAL:
            return eval()
        if self is SpanType.TASK:
            return task()
        if self is SpanType.TOOL:
            return tool()
        if self is SpanType.AUTOMATION:
            return automation()
        if self is SpanType.FACET:
            return facet()
        if self is SpanType.PREPROCESSOR:
            return preprocessor()
        if self is SpanType.CLASSIFIER:
            return classifier()
        if self is SpanType.REVIEW:
            return review()
