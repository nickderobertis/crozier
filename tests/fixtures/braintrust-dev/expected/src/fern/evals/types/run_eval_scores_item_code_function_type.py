

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class RunEvalScoresItemCodeFunctionType(enum.StrEnum):
    """
    The function type for inline code. Required when invoking inline preprocessors.
    """

    LLM = "llm"
    SCORER = "scorer"
    TASK = "task"
    TOOL = "tool"
    CUSTOM_VIEW = "custom_view"
    PREPROCESSOR = "preprocessor"
    FACET = "facet"
    CLASSIFIER = "classifier"
    TAG = "tag"
    PARAMETERS = "parameters"
    SANDBOX = "sandbox"

    def visit(
        self,
        llm: typing.Callable[[], T_Result],
        scorer: typing.Callable[[], T_Result],
        task: typing.Callable[[], T_Result],
        tool: typing.Callable[[], T_Result],
        custom_view: typing.Callable[[], T_Result],
        preprocessor: typing.Callable[[], T_Result],
        facet: typing.Callable[[], T_Result],
        classifier: typing.Callable[[], T_Result],
        tag: typing.Callable[[], T_Result],
        parameters: typing.Callable[[], T_Result],
        sandbox: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RunEvalScoresItemCodeFunctionType.LLM:
            return llm()
        if self is RunEvalScoresItemCodeFunctionType.SCORER:
            return scorer()
        if self is RunEvalScoresItemCodeFunctionType.TASK:
            return task()
        if self is RunEvalScoresItemCodeFunctionType.TOOL:
            return tool()
        if self is RunEvalScoresItemCodeFunctionType.CUSTOM_VIEW:
            return custom_view()
        if self is RunEvalScoresItemCodeFunctionType.PREPROCESSOR:
            return preprocessor()
        if self is RunEvalScoresItemCodeFunctionType.FACET:
            return facet()
        if self is RunEvalScoresItemCodeFunctionType.CLASSIFIER:
            return classifier()
        if self is RunEvalScoresItemCodeFunctionType.TAG:
            return tag()
        if self is RunEvalScoresItemCodeFunctionType.PARAMETERS:
            return parameters()
        if self is RunEvalScoresItemCodeFunctionType.SANDBOX:
            return sandbox()
