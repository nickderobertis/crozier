

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .comment_created_payload_payload import CommentCreatedPayloadPayload


class CommentCreatedPayload(UniversalBaseModel):
    """
    The Webhook payload for when a comment thread or reply is made on a Site
    """

    trigger_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="triggerType"),
        pydantic.Field(alias="triggerType", description="The type of event that triggered the request"),
    ] = None
    """
    The type of event that triggered the request
    """

    payload: typing.Optional[CommentCreatedPayloadPayload] = pydantic.Field(default=None)
    """
    The comment webhook payload contains data for the thread and for replies.  Check the type to determine if the payload is for a thread or a reply.  The webhook payload may be delayed by up to 5 minutes.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
