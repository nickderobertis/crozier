

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_l2vpn_termination import NestedL2VpnTermination
from .nested_role import NestedRole
from .nested_site import NestedSite
from .nested_tag import NestedTag
from .nested_tenant import NestedTenant
from .nested_vlan_group import NestedVlanGroup
from .vlan_status import VlanStatus


class Vlan(UniversalBaseModel):
    comments: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    description: typing.Optional[str] = None
    display: typing.Optional[str] = None
    group: typing.Optional[NestedVlanGroup] = None
    id: typing.Optional[int] = None
    l2vpn_termination: typing.Optional[NestedL2VpnTermination] = None
    last_updated: typing.Optional[dt.datetime] = None
    name: str
    prefix_count: typing.Optional[int] = None
    role: typing.Optional[NestedRole] = None
    site: typing.Optional[NestedSite] = None
    status: typing.Optional[VlanStatus] = None
    tags: typing.Optional[typing.List[NestedTag]] = None
    tenant: typing.Optional[NestedTenant] = None
    url: typing.Optional[str] = None
    vid: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
