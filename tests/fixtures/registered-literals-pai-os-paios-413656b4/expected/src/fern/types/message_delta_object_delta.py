

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_delta_object_delta_content_item import MessageDeltaObjectDeltaContentItem
from .message_delta_object_delta_role import MessageDeltaObjectDeltaRole


class MessageDeltaObjectDelta(UniversalBaseModel):
    """
    The delta containing the fields that have changed on the Message.
    """

    role: typing.Optional[MessageDeltaObjectDeltaRole] = pydantic.Field(default=None)
    """
    The entity that produced the message. One of `user` or `assistant`.
    """

    content: typing.Optional[typing.List[MessageDeltaObjectDeltaContentItem]] = pydantic.Field(default=None)
    """
    The content of the message in array of text and/or images.
    """

    file_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of [file](/docs/api-reference/files) IDs that the assistant should use. Useful for tools like retrieval and code_interpreter that can access files. A maximum of 10 files can be attached to a message.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
