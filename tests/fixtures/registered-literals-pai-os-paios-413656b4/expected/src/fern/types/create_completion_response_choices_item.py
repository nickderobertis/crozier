

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_completion_response_choices_item_finish_reason import CreateCompletionResponseChoicesItemFinishReason
from .create_completion_response_choices_item_logprobs import CreateCompletionResponseChoicesItemLogprobs


class CreateCompletionResponseChoicesItem(UniversalBaseModel):
    finish_reason: CreateCompletionResponseChoicesItemFinishReason = pydantic.Field()
    """
    The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,
    `length` if the maximum number of tokens specified in the request was reached,
    or `content_filter` if content was omitted due to a flag from our content filters.
    """

    index: int
    logprobs: typing.Optional[CreateCompletionResponseChoicesItemLogprobs] = None
    text: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
