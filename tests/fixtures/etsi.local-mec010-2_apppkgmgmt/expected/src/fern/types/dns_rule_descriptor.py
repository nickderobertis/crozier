

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ip_address_type import IpAddressType


class DnsRuleDescriptor(UniversalBaseModel):
    dns_rule_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="dnsRuleId"), pydantic.Field(alias="dnsRuleId", description="Identifies the DNS Rule")
    ]
    """
    Identifies the DNS Rule
    """

    domain_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="domainName"), pydantic.Field(alias="domainName", description="FQDN of the DNS rule")
    ]
    """
    FQDN of the DNS rule
    """

    ip_address: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="ipAddress"),
        pydantic.Field(alias="ipAddress", description="IP address given by the DNS rule"),
    ]
    """
    IP address given by the DNS rule
    """

    ip_address_type: typing_extensions.Annotated[
        IpAddressType, FieldMetadata(alias="ipAddressType"), pydantic.Field(alias="ipAddressType")
    ]
    ttl: typing.Optional[int] = pydantic.Field(default=None)
    """
    Time-to-live value
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
