

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .truncation_object_type import TruncationObjectType


class TruncationObject(UniversalBaseModel):
    type: typing.Optional[TruncationObjectType] = pydantic.Field(default=None)
    """
    The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.
    """

    last_messages: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of most recent messages from the thread when constructing the context for the run.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
