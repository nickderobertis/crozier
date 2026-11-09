

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_file_object_object import MessageFileObjectObject


class MessageFileObject(UniversalBaseModel):
    """
    A list of files attached to a `message`.
    """

    id: str = pydantic.Field()
    """
    The identifier, which can be referenced in API endpoints.
    """

    object: MessageFileObjectObject = pydantic.Field()
    """
    The object type, which is always `thread.message.file`.
    """

    created_at: int = pydantic.Field()
    """
    The Unix timestamp (in seconds) for when the message file was created.
    """

    message_id: str = pydantic.Field()
    """
    The ID of the [message](/docs/api-reference/messages) that the [File](/docs/api-reference/files) is attached to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
