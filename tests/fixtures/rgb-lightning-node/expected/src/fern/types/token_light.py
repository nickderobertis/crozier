

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .media import Media


class TokenLight(UniversalBaseModel):
    index: int
    ticker: typing.Optional[str] = None
    name: typing.Optional[str] = None
    details: typing.Optional[str] = None
    embedded_media: bool
    media: typing.Optional[Media] = None
    attachments: typing.Dict[str, Media]
    reserves: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
