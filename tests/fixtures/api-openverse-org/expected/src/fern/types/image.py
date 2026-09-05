

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tag import Tag


class Image(UniversalBaseModel):
    id: typing.Optional[str] = None
    title: typing.Optional[str] = None
    creator: typing.Optional[str] = None
    creator_url: typing.Optional[str] = None
    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Direct URL to the media file
    """

    foreign_landing_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of the source page
    """

    detail_url: typing.Optional[str] = None
    related_url: typing.Optional[str] = None
    license: typing.Optional[str] = pydantic.Field(default=None)
    """
    License identifier (e.g., by, by-nc, cc0, pdm)
    """

    license_version: typing.Optional[str] = None
    license_url: typing.Optional[str] = None
    provider: typing.Optional[str] = None
    source: typing.Optional[str] = None
    thumbnail: typing.Optional[str] = None
    width: typing.Optional[int] = None
    height: typing.Optional[int] = None
    tags: typing.Optional[typing.List[Tag]] = None
    attribution: typing.Optional[str] = None
    fields_matched: typing.Optional[typing.List[str]] = None
    mature: typing.Optional[bool] = None
    indexed_on: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
