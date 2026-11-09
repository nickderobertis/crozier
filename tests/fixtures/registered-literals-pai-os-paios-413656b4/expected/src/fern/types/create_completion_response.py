

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .completion_usage import CompletionUsage
from .create_completion_response_choices_item import CreateCompletionResponseChoicesItem
from .create_completion_response_object import CreateCompletionResponseObject


class CreateCompletionResponse(UniversalBaseModel):
    """
    Represents a completion response from the API. Note: both the streamed and non-streamed response objects share the same shape (unlike the chat endpoint).
    """

    id: str = pydantic.Field()
    """
    A unique identifier for the completion.
    """

    choices: typing.List[CreateCompletionResponseChoicesItem] = pydantic.Field()
    """
    The list of completion choices the model generated for the input prompt.
    """

    created: int = pydantic.Field()
    """
    The Unix timestamp (in seconds) of when the completion was created.
    """

    model: str = pydantic.Field()
    """
    The model used for completion.
    """

    system_fingerprint: typing.Optional[str] = pydantic.Field(default=None)
    """
    This fingerprint represents the backend configuration that the model runs with.
    
    Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.
    """

    object: CreateCompletionResponseObject = pydantic.Field()
    """
    The object type, which is always "text_completion"
    """

    usage: typing.Optional[CompletionUsage] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
