

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_embed_author_response import MessageEmbedAuthorResponse
from .message_embed_field_response import MessageEmbedFieldResponse
from .message_embed_footer_response import MessageEmbedFooterResponse
from .message_embed_image_response import MessageEmbedImageResponse
from .message_embed_provider_response import MessageEmbedProviderResponse
from .message_embed_video_response import MessageEmbedVideoResponse


class MessageEmbedResponse(UniversalBaseModel):
    type: str
    url: typing.Optional[str] = None
    title: typing.Optional[str] = None
    description: typing.Optional[str] = None
    color: typing.Optional[int] = None
    timestamp: typing.Optional[dt.datetime] = None
    fields: typing.Optional[typing.List[MessageEmbedFieldResponse]] = None
    author: typing.Optional[MessageEmbedAuthorResponse] = None
    provider: typing.Optional[MessageEmbedProviderResponse] = None
    image: typing.Optional[MessageEmbedImageResponse] = None
    thumbnail: typing.Optional[MessageEmbedImageResponse] = None
    video: typing.Optional[MessageEmbedVideoResponse] = None
    footer: typing.Optional[MessageEmbedFooterResponse] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
