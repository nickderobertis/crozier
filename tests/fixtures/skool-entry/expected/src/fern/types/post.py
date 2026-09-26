

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Post(UniversalBaseModel):
    id: typing.Optional[str] = None
    title: typing.Optional[str] = None
    content: typing.Optional[str] = None
    author: typing.Optional[typing.Dict[str, typing.Any]] = None
    group: typing.Optional[str] = None
    category: typing.Optional[str] = None
    likes: typing.Optional[int] = None
    comments_count: typing.Optional[int] = None
    created_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
