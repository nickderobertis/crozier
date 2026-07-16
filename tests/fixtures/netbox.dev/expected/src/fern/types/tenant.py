

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_tag import NestedTag
from .nested_tenant_group import NestedTenantGroup


class Tenant(UniversalBaseModel):
    circuit_count: typing.Optional[int] = None
    cluster_count: typing.Optional[int] = None
    comments: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    description: typing.Optional[str] = None
    device_count: typing.Optional[int] = None
    display: typing.Optional[str] = None
    group: typing.Optional[NestedTenantGroup] = None
    id: typing.Optional[int] = None
    ipaddress_count: typing.Optional[int] = None
    last_updated: typing.Optional[dt.datetime] = None
    name: str
    prefix_count: typing.Optional[int] = None
    rack_count: typing.Optional[int] = None
    site_count: typing.Optional[int] = None
    slug: str
    tags: typing.Optional[typing.List[NestedTag]] = None
    url: typing.Optional[str] = None
    virtualmachine_count: typing.Optional[int] = None
    vlan_count: typing.Optional[int] = None
    vrf_count: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
