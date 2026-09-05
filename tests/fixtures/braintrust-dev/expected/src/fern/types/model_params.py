

import typing

from .model_params_frequency_penalty import ModelParamsFrequencyPenalty
from .model_params_max_output_tokens import ModelParamsMaxOutputTokens
from .model_params_max_tokens_to_sample import ModelParamsMaxTokensToSample
from .model_params_reasoning_budget import ModelParamsReasoningBudget
from .model_params_three import ModelParamsThree

ModelParams = typing.Union[
    ModelParamsFrequencyPenalty,
    ModelParamsMaxTokensToSample,
    ModelParamsMaxOutputTokens,
    ModelParamsThree,
    ModelParamsReasoningBudget,
]
