

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .model_params_frequency_penalty_tool_choice_function_function import (
    ModelParamsFrequencyPenaltyToolChoiceFunctionFunction,
)
from .model_params_frequency_penalty_tool_choice_function_type import ModelParamsFrequencyPenaltyToolChoiceFunctionType


class ModelParamsFrequencyPenaltyToolChoiceFunction(UniversalBaseModel):
    type: ModelParamsFrequencyPenaltyToolChoiceFunctionType
    function: ModelParamsFrequencyPenaltyToolChoiceFunctionFunction

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
