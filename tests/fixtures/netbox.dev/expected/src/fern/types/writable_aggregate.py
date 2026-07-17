

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_tag import NestedTag


class WritableAggregate(UniversalBaseModel):
    comments: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = None
    date_added: typing.Optional[dt.date] = None
    description: typing.Optional[str] = None
    display: typing.Optional[str] = None
    family: typing.Optional[str] = None
    id: typing.Optional[int] = None
    last_updated: typing.Optional[dt.datetime] = None
    prefix: str
    rir: int
    tags: typing.Optional[typing.List[NestedTag]] = None
    tenant: typing.Optional[int] = None
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
