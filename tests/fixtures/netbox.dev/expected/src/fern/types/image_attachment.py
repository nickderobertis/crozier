

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ImageAttachment(UniversalBaseModel):
    content_type: str
    created: typing.Optional[dt.datetime] = None
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    image: typing.Optional[str] = None
    image_height: int
    image_width: int
    last_updated: typing.Optional[dt.datetime] = None
    name: typing.Optional[str] = None
    object_id: int
    parent: typing.Optional[typing.Dict[str, typing.Any]] = None
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
