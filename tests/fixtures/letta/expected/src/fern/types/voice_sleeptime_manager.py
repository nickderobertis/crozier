

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class VoiceSleeptimeManager(UniversalBaseModel):
    manager_agent_id: str = pydantic.Field()
    """
    
    """

    max_message_buffer_length: typing.Optional[int] = pydantic.Field(default=None)
    """
    The desired maximum length of messages in the context window of the convo agent. This is a best effort, and may be off slightly due to user/assistant interleaving.
    """

    min_message_buffer_length: typing.Optional[int] = pydantic.Field(default=None)
    """
    The desired minimum length of messages in the context window of the convo agent. This is a best effort, and may be off-by-one due to user/assistant interleaving.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
