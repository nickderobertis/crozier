

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FunctionTypeEnumNullish(enum.StrEnum):
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
        if self is FunctionTypeEnumNullish.LLM:
            return llm()
        if self is FunctionTypeEnumNullish.SCORER:
            return scorer()
        if self is FunctionTypeEnumNullish.TASK:
            return task()
        if self is FunctionTypeEnumNullish.TOOL:
            return tool()
        if self is FunctionTypeEnumNullish.CUSTOM_VIEW:
            return custom_view()
        if self is FunctionTypeEnumNullish.PREPROCESSOR:
            return preprocessor()
        if self is FunctionTypeEnumNullish.FACET:
            return facet()
        if self is FunctionTypeEnumNullish.CLASSIFIER:
            return classifier()
        if self is FunctionTypeEnumNullish.TAG:
            return tag()
        if self is FunctionTypeEnumNullish.PARAMETERS:
            return parameters()
        if self is FunctionTypeEnumNullish.SANDBOX:
            return sandbox()
