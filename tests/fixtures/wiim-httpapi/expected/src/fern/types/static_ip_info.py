

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class StaticIpInfo(UniversalBaseModel):
    wlan_static_ip: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="wlanStaticIp"),
        pydantic.Field(alias="wlanStaticIp", description="Wifi IP address of the device"),
    ] = None
    """
    Wifi IP address of the device
    """

    wlan_gate_way: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="wlanGateWay"),
        pydantic.Field(alias="wlanGateWay", description="Wifi IP address of the gateway"),
    ] = None
    """
    Wifi IP address of the gateway
    """

    wlan_dns_server: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="wlanDnsServer"),
        pydantic.Field(alias="wlanDnsServer", description="Wifi IP address of the DNS server"),
    ] = None
    """
    Wifi IP address of the DNS server
    """

    wlan_static_ip_enable: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="wlanStaticIpEnable"),
        pydantic.Field(
            alias="wlanStaticIpEnable",
            description="Status of the WiFi static IP configuration\n0: Disabled\n1: Enabled",
        ),
    ] = None
    """
    Status of the WiFi static IP configuration
    0: Disabled
    1: Enabled
    """

    eth_static_ip: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ethStaticIp"),
        pydantic.Field(alias="ethStaticIp", description="Wired IP address of the device"),
    ] = None
    """
    Wired IP address of the device
    """

    eth_gate_way: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ethGateWay"),
        pydantic.Field(alias="ethGateWay", description="Wired IP address of the gateway"),
    ] = None
    """
    Wired IP address of the gateway
    """

    eth_dns_server: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ethDnsServer"),
        pydantic.Field(alias="ethDnsServer", description="Wired IP address of the DNS server"),
    ] = None
    """
    Wired IP address of the DNS server
    """

    eth_static_ip_enable: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ethStaticIpEnable"),
        pydantic.Field(
            alias="ethStaticIpEnable",
            description="Status of the wired static IP configuration\n0: Disabled\n1: Enabled",
        ),
    ] = None
    """
    Status of the wired static IP configuration
    0: Disabled
    1: Enabled
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
