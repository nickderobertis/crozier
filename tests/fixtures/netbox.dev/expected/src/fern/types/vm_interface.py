

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_l2vpn_termination import NestedL2VpnTermination
from .nested_tag import NestedTag
from .nested_virtual_machine import NestedVirtualMachine
from .nested_vlan import NestedVlan
from .nested_vm_interface import NestedVmInterface
from .nested_vrf import NestedVrf
from .vm_interface_mode import VmInterfaceMode


class VmInterface(UniversalBaseModel):
    bridge: typing.Optional[NestedVmInterface] = None
    count_fhrp_groups: typing.Optional[int] = None
    count_ipaddresses: typing.Optional[int] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    description: typing.Optional[str] = None
    display: typing.Optional[str] = None
    enabled: typing.Optional[bool] = None
    id: typing.Optional[int] = None
    l2vpn_termination: typing.Optional[NestedL2VpnTermination] = None
    last_updated: typing.Optional[dt.datetime] = None
    mac_address: typing.Optional[str] = None
    mode: typing.Optional[VmInterfaceMode] = None
    mtu: typing.Optional[int] = None
    name: str
    parent: typing.Optional[NestedVmInterface] = None
    tagged_vlans: typing.Optional[typing.List[typing.Optional[NestedVlan]]] = None
    tags: typing.Optional[typing.List[NestedTag]] = None
    untagged_vlan: typing.Optional[NestedVlan] = None
    url: typing.Optional[str] = None
    virtual_machine: typing.Optional[NestedVirtualMachine] = None
    vrf: typing.Optional[NestedVrf] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
