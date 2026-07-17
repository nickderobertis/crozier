

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .component_nested_module import ComponentNestedModule
from .interface_duplex import InterfaceDuplex
from .interface_mode import InterfaceMode
from .interface_poe_mode import InterfacePoeMode
from .interface_poe_type import InterfacePoeType
from .interface_rf_channel import InterfaceRfChannel
from .interface_rf_role import InterfaceRfRole
from .interface_type import InterfaceType
from .nested_cable import NestedCable
from .nested_device import NestedDevice
from .nested_interface import NestedInterface
from .nested_l2vpn_termination import NestedL2VpnTermination
from .nested_tag import NestedTag
from .nested_virtual_device_context import NestedVirtualDeviceContext
from .nested_vlan import NestedVlan
from .nested_vrf import NestedVrf
from .nested_wireless_lan import NestedWirelessLan
from .nested_wireless_link import NestedWirelessLink


class Interface(UniversalBaseModel):
    occupied: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="_occupied"), pydantic.Field(alias="_occupied")
    ] = None
    bridge: typing.Optional[NestedInterface] = None
    cable: typing.Optional[NestedCable] = None
    cable_end: typing.Optional[str] = None
    connected_endpoints: typing.Optional[typing.List[typing.Optional[str]]] = pydantic.Field(default=None)
    """
    
    Return the appropriate serializer for the type of connected object.
    """

    connected_endpoints_reachable: typing.Optional[bool] = None
    connected_endpoints_type: typing.Optional[str] = None
    count_fhrp_groups: typing.Optional[int] = None
    count_ipaddresses: typing.Optional[int] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = None
    description: typing.Optional[str] = None
    device: NestedDevice
    display: typing.Optional[str] = None
    duplex: typing.Optional[InterfaceDuplex] = None
    enabled: typing.Optional[bool] = None
    id: typing.Optional[int] = None
    l2vpn_termination: typing.Optional[NestedL2VpnTermination] = None
    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Physical label
    """

    lag: typing.Optional[NestedInterface] = None
    last_updated: typing.Optional[dt.datetime] = None
    link_peers: typing.Optional[typing.List[typing.Optional[str]]] = pydantic.Field(default=None)
    """
    
    Return the appropriate serializer for the link termination model.
    """

    link_peers_type: typing.Optional[str] = None
    mac_address: typing.Optional[str] = None
    mark_connected: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Treat as if a cable is connected
    """

    mgmt_only: typing.Optional[bool] = pydantic.Field(default=None)
    """
    This interface is used only for out-of-band management
    """

    mode: typing.Optional[InterfaceMode] = None
    module: typing.Optional[ComponentNestedModule] = None
    mtu: typing.Optional[int] = None
    name: str
    parent: typing.Optional[NestedInterface] = None
    poe_mode: typing.Optional[InterfacePoeMode] = None
    poe_type: typing.Optional[InterfacePoeType] = None
    rf_channel: typing.Optional[InterfaceRfChannel] = None
    rf_channel_frequency: typing.Optional[float] = None
    rf_channel_width: typing.Optional[float] = None
    rf_role: typing.Optional[InterfaceRfRole] = None
    speed: typing.Optional[int] = None
    tagged_vlans: typing.Optional[typing.List[typing.Optional[NestedVlan]]] = None
    tags: typing.Optional[typing.List[NestedTag]] = None
    tx_power: typing.Optional[int] = None
    type: InterfaceType
    untagged_vlan: typing.Optional[NestedVlan] = None
    url: typing.Optional[str] = None
    vdcs: typing.Optional[typing.List[NestedVirtualDeviceContext]] = None
    vrf: typing.Optional[NestedVrf] = None
    wireless_lans: typing.Optional[typing.List[NestedWirelessLan]] = None
    wireless_link: typing.Optional[NestedWirelessLink] = None
    wwn: typing.Optional[str] = pydantic.Field(default=None)
    """
    64-bit World Wide Name
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
