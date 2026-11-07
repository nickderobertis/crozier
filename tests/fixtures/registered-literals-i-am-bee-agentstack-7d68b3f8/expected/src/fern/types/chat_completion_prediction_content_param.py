

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_prediction_content_param_content import ChatCompletionPredictionContentParamContent
from .chat_completion_prediction_content_param_type import ChatCompletionPredictionContentParamType


class ChatCompletionPredictionContentParam(UniversalBaseModel):
    """
    Static predicted output content, such as the content of a text file that is
    being regenerated.
    """

    content: ChatCompletionPredictionContentParamContent
    type: ChatCompletionPredictionContentParamType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
