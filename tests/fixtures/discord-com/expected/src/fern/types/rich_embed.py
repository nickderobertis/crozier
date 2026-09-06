

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .rich_embed_author import RichEmbedAuthor
from .rich_embed_field import RichEmbedField
from .rich_embed_footer import RichEmbedFooter
from .rich_embed_image import RichEmbedImage
from .rich_embed_provider import RichEmbedProvider
from .rich_embed_thumbnail import RichEmbedThumbnail
from .rich_embed_video import RichEmbedVideo


class RichEmbed(UniversalBaseModel):
    type: typing.Optional[str] = None
    url: typing.Optional[str] = None
    title: typing.Optional[str] = None
    color: typing.Optional[int] = None
    timestamp: typing.Optional[dt.datetime] = None
    description: typing.Optional[str] = None
    author: typing.Optional[RichEmbedAuthor] = None
    image: typing.Optional[RichEmbedImage] = None
    thumbnail: typing.Optional[RichEmbedThumbnail] = None
    footer: typing.Optional[RichEmbedFooter] = None
    fields: typing.Optional[typing.List[RichEmbedField]] = None
    provider: typing.Optional[RichEmbedProvider] = None
    video: typing.Optional[RichEmbedVideo] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
