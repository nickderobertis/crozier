

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .nested_cable import NestedCable
from .nested_tag import NestedTag
from .writable_interface_duplex import WritableInterfaceDuplex
from .writable_interface_mode import WritableInterfaceMode
from .writable_interface_poe_mode import WritableInterfacePoeMode
from .writable_interface_poe_type import WritableInterfacePoeType
from .writable_interface_rf_channel import WritableInterfaceRfChannel
from .writable_interface_rf_role import WritableInterfaceRfRole
from .writable_interface_type import WritableInterfaceType


class WritableInterface(UniversalBaseModel):
    occupied: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="_occupied"), pydantic.Field(alias="_occupied")
    ] = None
    bridge: typing.Optional[int] = None
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
    device: int
    display: typing.Optional[str] = None
    duplex: typing.Optional[WritableInterfaceDuplex] = None
    enabled: typing.Optional[bool] = None
    id: typing.Optional[int] = None
    l2vpn_termination: typing.Optional[str] = None
    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Physical label
    """

    lag: typing.Optional[int] = None
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

    mode: typing.Optional[WritableInterfaceMode] = None
    module: typing.Optional[int] = None
    mtu: typing.Optional[int] = None
    name: str
    parent: typing.Optional[int] = None
    poe_mode: typing.Optional[WritableInterfacePoeMode] = None
    poe_type: typing.Optional[WritableInterfacePoeType] = None
    rf_channel: typing.Optional[WritableInterfaceRfChannel] = None
    rf_channel_frequency: typing.Optional[float] = None
    rf_channel_width: typing.Optional[float] = None
    rf_role: typing.Optional[WritableInterfaceRfRole] = None
    speed: typing.Optional[int] = None
    tagged_vlans: typing.Optional[typing.List[int]] = None
    tags: typing.Optional[typing.List[NestedTag]] = None
    tx_power: typing.Optional[int] = None
    type: WritableInterfaceType
    untagged_vlan: typing.Optional[int] = None
    url: typing.Optional[str] = None
    vdcs: typing.List[int]
    vrf: typing.Optional[int] = None
    wireless_lans: typing.Optional[typing.List[int]] = None
    wireless_link: typing.Optional[int] = None
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
