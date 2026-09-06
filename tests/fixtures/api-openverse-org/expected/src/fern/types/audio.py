

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tag import Tag


class Audio(UniversalBaseModel):
    id: typing.Optional[str] = None
    title: typing.Optional[str] = None
    creator: typing.Optional[str] = None
    creator_url: typing.Optional[str] = None
    url: typing.Optional[str] = None
    foreign_landing_url: typing.Optional[str] = None
    detail_url: typing.Optional[str] = None
    related_url: typing.Optional[str] = None
    license: typing.Optional[str] = None
    license_version: typing.Optional[str] = None
    license_url: typing.Optional[str] = None
    provider: typing.Optional[str] = None
    source: typing.Optional[str] = None
    thumbnail: typing.Optional[str] = None
    duration: typing.Optional[int] = pydantic.Field(default=None)
    """
    Duration in milliseconds
    """

    bit_rate: typing.Optional[int] = None
    sample_rate: typing.Optional[int] = None
    genres: typing.Optional[typing.List[str]] = None
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
