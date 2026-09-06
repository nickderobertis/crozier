

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .webhook_slack_embed_field import WebhookSlackEmbedField


class WebhookSlackEmbed(UniversalBaseModel):
    title: typing.Optional[str] = None
    title_link: typing.Optional[str] = None
    text: typing.Optional[str] = None
    color: typing.Optional[str] = None
    ts: typing.Optional[int] = None
    pretext: typing.Optional[str] = None
    footer: typing.Optional[str] = None
    footer_icon: typing.Optional[str] = None
    author_name: typing.Optional[str] = None
    author_link: typing.Optional[str] = None
    author_icon: typing.Optional[str] = None
    image_url: typing.Optional[str] = None
    thumb_url: typing.Optional[str] = None
    fields: typing.Optional[typing.List[WebhookSlackEmbedField]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
