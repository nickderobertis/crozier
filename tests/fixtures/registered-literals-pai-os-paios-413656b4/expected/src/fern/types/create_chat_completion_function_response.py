

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .completion_usage import CompletionUsage
from .create_chat_completion_function_response_choices_item import CreateChatCompletionFunctionResponseChoicesItem
from .create_chat_completion_function_response_object import CreateChatCompletionFunctionResponseObject


class CreateChatCompletionFunctionResponse(UniversalBaseModel):
    """
    Represents a chat completion response returned by model, based on the provided input.
    """

    id: str = pydantic.Field()
    """
    A unique identifier for the chat completion.
    """

    choices: typing.List[CreateChatCompletionFunctionResponseChoicesItem] = pydantic.Field()
    """
    A list of chat completion choices. Can be more than one if `n` is greater than 1.
    """

    created: int = pydantic.Field()
    """
    The Unix timestamp (in seconds) of when the chat completion was created.
    """

    model: str = pydantic.Field()
    """
    The model used for the chat completion.
    """

    system_fingerprint: typing.Optional[str] = pydantic.Field(default=None)
    """
    This fingerprint represents the backend configuration that the model runs with.
    
    Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.
    """

    object: CreateChatCompletionFunctionResponseObject = pydantic.Field()
    """
    The object type, which is always `chat.completion`.
    """

    usage: typing.Optional[CompletionUsage] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
