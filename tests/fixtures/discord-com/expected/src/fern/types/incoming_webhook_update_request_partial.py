

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .action_row_component_for_message_request import ActionRowComponentForMessageRequest
from .message_allowed_mentions_request import MessageAllowedMentionsRequest
from .message_attachment_request import MessageAttachmentRequest
from .poll_create_request import PollCreateRequest
from .rich_embed import RichEmbed


class IncomingWebhookUpdateRequestPartial(UniversalBaseModel):
    content: typing.Optional[str] = None
    embeds: typing.Optional[typing.List[RichEmbed]] = None
    allowed_mentions: typing.Optional[MessageAllowedMentionsRequest] = None
    components: typing.Optional[typing.List[ActionRowComponentForMessageRequest]] = None
    attachments: typing.Optional[typing.List[MessageAttachmentRequest]] = None
    poll: typing.Optional[PollCreateRequest] = None
    flags: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
