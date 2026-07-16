

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_tag import NestedTag
from .writable_vm_interface_mode import WritableVmInterfaceMode


class WritableVmInterface(UniversalBaseModel):
    bridge: typing.Optional[int] = None
    count_fhrp_groups: typing.Optional[int] = None
    count_ipaddresses: typing.Optional[int] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    description: typing.Optional[str] = None
    display: typing.Optional[str] = None
    enabled: typing.Optional[bool] = None
    id: typing.Optional[int] = None
    l2vpn_termination: typing.Optional[str] = None
    last_updated: typing.Optional[dt.datetime] = None
    mac_address: typing.Optional[str] = None
    mode: typing.Optional[WritableVmInterfaceMode] = None
    mtu: typing.Optional[int] = None
    name: str
    parent: typing.Optional[int] = None
    tagged_vlans: typing.Optional[typing.List[int]] = None
    tags: typing.Optional[typing.List[NestedTag]] = None
    untagged_vlan: typing.Optional[int] = None
    url: typing.Optional[str] = None
    virtual_machine: int
    vrf: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
