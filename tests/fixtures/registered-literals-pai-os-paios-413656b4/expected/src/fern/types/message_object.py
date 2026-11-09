

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_object_content_item import MessageObjectContentItem
from .message_object_incomplete_details import MessageObjectIncompleteDetails
from .message_object_object import MessageObjectObject
from .message_object_role import MessageObjectRole
from .message_object_status import MessageObjectStatus


class MessageObject(UniversalBaseModel):
    """
    Represents a message within a [thread](/docs/api-reference/threads).
    """

    id: str = pydantic.Field()
    """
    The identifier, which can be referenced in API endpoints.
    """

    object: MessageObjectObject = pydantic.Field()
    """
    The object type, which is always `thread.message`.
    """

    created_at: int = pydantic.Field()
    """
    The Unix timestamp (in seconds) for when the message was created.
    """

    thread_id: str = pydantic.Field()
    """
    The [thread](/docs/api-reference/threads) ID that this message belongs to.
    """

    status: MessageObjectStatus = pydantic.Field()
    """
    The status of the message, which can be either `in_progress`, `incomplete`, or `completed`.
    """

    incomplete_details: typing.Optional[MessageObjectIncompleteDetails] = pydantic.Field(default=None)
    """
    On an incomplete message, details about why the message is incomplete.
    """

    completed_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    The Unix timestamp (in seconds) for when the message was completed.
    """

    incomplete_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    The Unix timestamp (in seconds) for when the message was marked as incomplete.
    """

    role: MessageObjectRole = pydantic.Field()
    """
    The entity that produced the message. One of `user` or `assistant`.
    """

    content: typing.List[MessageObjectContentItem] = pydantic.Field()
    """
    The content of the message in array of text and/or images.
    """

    assistant_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    If applicable, the ID of the [assistant](/docs/api-reference/assistants) that authored this message.
    """

    run_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the [run](/docs/api-reference/runs) associated with the creation of this message. Value is `null` when messages are created manually using the create message or create thread endpoints.
    """

    file_ids: typing.List[str] = pydantic.Field()
    """
    A list of [file](/docs/api-reference/files) IDs that the assistant should use. Useful for tools like retrieval and code_interpreter that can access files. A maximum of 10 files can be attached to a message.
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
