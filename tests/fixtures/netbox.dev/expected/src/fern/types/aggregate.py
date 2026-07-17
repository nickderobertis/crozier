

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .aggregate_family import AggregateFamily
from .nested_rir import NestedRir
from .nested_tag import NestedTag
from .nested_tenant import NestedTenant


class Aggregate(UniversalBaseModel):
    comments: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = None
    date_added: typing.Optional[dt.date] = None
    description: typing.Optional[str] = None
    display: typing.Optional[str] = None
    family: typing.Optional[AggregateFamily] = None
    id: typing.Optional[int] = None
    last_updated: typing.Optional[dt.datetime] = None
    prefix: str
    rir: NestedRir
    tags: typing.Optional[typing.List[NestedTag]] = None
    tenant: typing.Optional[NestedTenant] = None
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
