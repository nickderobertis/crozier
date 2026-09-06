

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FunctionTypeEnum(enum.StrEnum):
    """
    The type of global function. Defaults to 'scorer'.
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
        if self is FunctionTypeEnum.LLM:
            return llm()
        if self is FunctionTypeEnum.SCORER:
            return scorer()
        if self is FunctionTypeEnum.TASK:
            return task()
        if self is FunctionTypeEnum.TOOL:
            return tool()
        if self is FunctionTypeEnum.CUSTOM_VIEW:
            return custom_view()
        if self is FunctionTypeEnum.PREPROCESSOR:
            return preprocessor()
        if self is FunctionTypeEnum.FACET:
            return facet()
        if self is FunctionTypeEnum.CLASSIFIER:
            return classifier()
        if self is FunctionTypeEnum.TAG:
            return tag()
        if self is FunctionTypeEnum.PARAMETERS:
            return parameters()
        if self is FunctionTypeEnum.SANDBOX:
            return sandbox()
