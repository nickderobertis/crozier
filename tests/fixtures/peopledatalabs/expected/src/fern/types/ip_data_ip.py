

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .company_location import CompanyLocation
from .ip_data_ip_metadata import IpDataIpMetadata


class IpDataIp(UniversalBaseModel):
    """
    Information related to the IP address.
    """

    address: typing.Optional[str] = pydantic.Field(default=None)
    """
    The matched IP address.
    """

    metadata: typing.Optional[IpDataIpMetadata] = pydantic.Field(default=None)
    """
    Premium fields targeted towards identifying IPs as mobile or using hosting, proxy, Tor, VPN, relay or other services.
    """

    location: typing.Optional[CompanyLocation] = pydantic.Field(default=None)
    """
    The location associated with the IP address.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
