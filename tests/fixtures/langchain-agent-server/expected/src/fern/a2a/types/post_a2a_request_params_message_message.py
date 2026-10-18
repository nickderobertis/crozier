

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_a2a_request_params_message_message_parts_item import PostA2ARequestParamsMessageMessagePartsItem
from .post_a2a_request_params_message_message_role import PostA2ARequestParamsMessageMessageRole


class PostA2ARequestParamsMessageMessage(UniversalBaseModel):
    role: PostA2ARequestParamsMessageMessageRole = pydantic.Field()
    """
    A2A role for the message sender.
    """

    parts: typing.List[PostA2ARequestParamsMessageMessagePartsItem] = pydantic.Field()
    """
    Message parts (text/data only).
    """

    message_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="messageId"),
        pydantic.Field(alias="messageId", description="Client-generated message identifier."),
    ]
    """
    Client-generated message identifier.
    """

    context_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="contextId"),
        pydantic.Field(alias="contextId", description="Conversation context ID; maps to LangGraph thread_id."),
    ] = None
    """
    Conversation context ID; maps to LangGraph thread_id.
    """

    task_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="taskId"),
        pydantic.Field(alias="taskId", description="Optional task ID. Currently ignored by this implementation."),
    ] = None
    """
    Optional task ID. Currently ignored by this implementation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
