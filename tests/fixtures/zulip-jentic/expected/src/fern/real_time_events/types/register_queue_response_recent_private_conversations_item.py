

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RegisterQueueResponseRecentPrivateConversationsItem(UniversalBaseModel):
    """
    Object describing a single recent direct conversation in the user's history.
    """

    max_message_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The highest message ID of the conversation, intended to support sorting
    the conversations by recency.
    """

    user_ids: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    The list of users other than the current user in the direct message
    conversation. This will be an empty list for direct messages sent to
    oneself.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
