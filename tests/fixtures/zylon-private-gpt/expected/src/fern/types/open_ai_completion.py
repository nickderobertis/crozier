

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .open_ai_choice import OpenAiChoice
from .open_ai_completion_model import OpenAiCompletionModel
from .open_ai_completion_object import OpenAiCompletionObject


class OpenAiCompletion(UniversalBaseModel):
    """
    Clone of OpenAI Completion model.

    For more information see: https://platform.openai.com/docs/api-reference/chat/object
    """

    id: str
    object: typing.Optional[OpenAiCompletionObject] = None
    created: int
    model: OpenAiCompletionModel
    choices: typing.List[OpenAiChoice]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
