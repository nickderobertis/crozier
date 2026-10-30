

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dns_resolver import DnsResolver
from .nat_rule_tcp_ports_item import NatRuleTcpPortsItem


class NatRule(UniversalBaseModel):
    """
    Content of "simcore.service.containers-allowed-outgoing-permit-list" label
    """

    hostname: str
    tcp_ports: typing.List[NatRuleTcpPortsItem]
    dns_resolver: typing.Optional[DnsResolver] = pydantic.Field(default=None)
    """
    specify a DNS resolver address and port
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
