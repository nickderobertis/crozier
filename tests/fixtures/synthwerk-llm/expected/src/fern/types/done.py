

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .done_finish_reason import DoneFinishReason


class Done(UniversalBaseModel):
    """
    The last event of a stream that did not fail.
    """

    message_id: str = pydantic.Field()
    """
    Id of the stored assistant message.
    """

    finish_reason: DoneFinishReason = pydantic.Field()
    """
    - `stop`: the model finished the answer.
    - `length`: the answer hit the output token limit.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
