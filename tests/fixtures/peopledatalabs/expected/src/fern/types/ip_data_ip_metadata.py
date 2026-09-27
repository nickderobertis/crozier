

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class IpDataIpMetadata(UniversalBaseModel):
    """
    Premium fields targeted towards identifying IPs as mobile or using hosting, proxy, Tor, VPN, relay or other services.
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    The type of IP Address (IPv4 or IPv6).
    """

    mobile: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If the IP is a known mobile address.
    """

    hosting: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If the IP is a known hosting address.
    """

    proxy: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If the IP is a known proxy address.
    """

    tor: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If the IP is a known Tor address.
    """

    vpn: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If the IP is a known VPN address.
    """

    relay: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If the IP is a known relay address.
    """

    service: typing.Optional[str] = pydantic.Field(default=None)
    """
    If known, the name of the service for the address.
    """

    asn_domain: typing.Optional[str] = pydantic.Field(default=None)
    """
    The domain associated with the ASN block.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
