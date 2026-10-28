

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .provider import Provider


class ItemProperties(UniversalBaseModel):
    """
    https://github.com/radiantearth/stac-spec/blob/v1.0.0/item-spec/item-spec.md#properties-object
    """

    title: typing.Optional[str] = None
    description: typing.Optional[str] = None
    datetime: typing.Optional[dt.datetime] = None
    created: typing.Optional[dt.datetime] = None
    updated: typing.Optional[dt.datetime] = None
    start_datetime: typing.Optional[dt.datetime] = None
    end_datetime: typing.Optional[dt.datetime] = None
    license: typing.Optional[str] = None
    providers: typing.Optional[typing.List[Provider]] = None
    platform: typing.Optional[str] = None
    instruments: typing.Optional[typing.List[str]] = None
    constellation: typing.Optional[str] = None
    mission: typing.Optional[str] = None
    gsd: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
