

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_tag import NestedTag
from .writable_vlan_status import WritableVlanStatus


class WritableVlan(UniversalBaseModel):
    comments: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    description: typing.Optional[str] = None
    display: typing.Optional[str] = None
    group: typing.Optional[int] = None
    id: typing.Optional[int] = None
    l2vpn_termination: typing.Optional[str] = None
    last_updated: typing.Optional[dt.datetime] = None
    name: str
    prefix_count: typing.Optional[int] = None
    role: typing.Optional[int] = None
    site: typing.Optional[int] = None
    status: typing.Optional[WritableVlanStatus] = None
    tags: typing.Optional[typing.List[NestedTag]] = None
    tenant: typing.Optional[int] = None
    url: typing.Optional[str] = None
    vid: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
