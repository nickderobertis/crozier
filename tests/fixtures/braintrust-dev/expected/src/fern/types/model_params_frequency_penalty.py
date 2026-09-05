

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .model_params_frequency_penalty_function_call import ModelParamsFrequencyPenaltyFunctionCall
from .model_params_frequency_penalty_reasoning_effort import ModelParamsFrequencyPenaltyReasoningEffort
from .model_params_frequency_penalty_tool_choice import ModelParamsFrequencyPenaltyToolChoice
from .model_params_frequency_penalty_verbosity import ModelParamsFrequencyPenaltyVerbosity
from .response_format_nullish import ResponseFormatNullish


class ModelParamsFrequencyPenalty(UniversalBaseModel):
    use_cache: typing.Optional[bool] = None
    reasoning_enabled: typing.Optional[bool] = None
    reasoning_budget: typing.Optional[float] = None
    temperature: typing.Optional[float] = None
    top_p: typing.Optional[float] = None
    max_tokens: typing.Optional[float] = None
    max_completion_tokens: typing.Optional[float] = pydantic.Field(default=None)
    """
    The successor to max_tokens
    """

    frequency_penalty: typing.Optional[float] = None
    presence_penalty: typing.Optional[float] = None
    response_format: typing.Optional[ResponseFormatNullish] = None
    tool_choice: typing.Optional[ModelParamsFrequencyPenaltyToolChoice] = None
    function_call: typing.Optional[ModelParamsFrequencyPenaltyFunctionCall] = None
    n: typing.Optional[float] = None
    stop: typing.Optional[typing.List[str]] = None
    reasoning_effort: typing.Optional[ModelParamsFrequencyPenaltyReasoningEffort] = None
    verbosity: typing.Optional[ModelParamsFrequencyPenaltyVerbosity] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
