

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .run_eval_scores_item_code_function_type import RunEvalScoresItemCodeFunctionType
from .run_eval_scores_item_code_inline_context import RunEvalScoresItemCodeInlineContext


class RunEvalScoresItemCode(UniversalBaseModel):
    """
    Inline code function
    """

    inline_context: RunEvalScoresItemCodeInlineContext
    code: str = pydantic.Field()
    """
    The inline code to execute
    """

    function_type: typing.Optional[RunEvalScoresItemCodeFunctionType] = pydantic.Field(default=None)
    """
    The function type for inline code. Required when invoking inline preprocessors.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the inline code function
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
