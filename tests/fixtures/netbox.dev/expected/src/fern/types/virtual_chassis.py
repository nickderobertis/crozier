

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_device import NestedDevice
from .nested_tag import NestedTag


class VirtualChassis(UniversalBaseModel):
    comments: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = None
    description: typing.Optional[str] = None
    display: typing.Optional[str] = None
    domain: typing.Optional[str] = None
    id: typing.Optional[int] = None
    last_updated: typing.Optional[dt.datetime] = None
    master: typing.Optional[NestedDevice] = None
    member_count: typing.Optional[int] = None
    name: str
    tags: typing.Optional[typing.List[NestedTag]] = None
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
