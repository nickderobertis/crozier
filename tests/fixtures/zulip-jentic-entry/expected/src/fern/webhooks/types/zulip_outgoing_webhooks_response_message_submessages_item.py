

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ZulipOutgoingWebhooksResponseMessageSubmessagesItem(UniversalBaseModel):
    msg_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of the message.
    """

    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    The new content of the submessage.
    """

    message_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the message to which the submessage has been added.
    """

    sender_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the user who sent the message.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the submessage.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
