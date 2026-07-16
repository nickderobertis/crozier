

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ip_address_family import IpAddressFamily
from .ip_address_role import IpAddressRole
from .ip_address_status import IpAddressStatus
from .nested_ip_address import NestedIpAddress
from .nested_tag import NestedTag
from .nested_tenant import NestedTenant
from .nested_vrf import NestedVrf


class IpAddress(UniversalBaseModel):
    address: str = pydantic.Field()
    """
    IPv4 or IPv6 address (with mask)
    """

    assigned_object: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    assigned_object_id: typing.Optional[int] = None
    assigned_object_type: typing.Optional[str] = None
    comments: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    description: typing.Optional[str] = None
    display: typing.Optional[str] = None
    dns_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Hostname or FQDN (not case-sensitive)
    """

    family: typing.Optional[IpAddressFamily] = None
    id: typing.Optional[int] = None
    last_updated: typing.Optional[dt.datetime] = None
    nat_inside: typing.Optional[NestedIpAddress] = None
    nat_outside: typing.Optional[typing.List[NestedIpAddress]] = None
    role: typing.Optional[IpAddressRole] = None
    status: typing.Optional[IpAddressStatus] = None
    tags: typing.Optional[typing.List[NestedTag]] = None
    tenant: typing.Optional[NestedTenant] = None
    url: typing.Optional[str] = None
    vrf: typing.Optional[NestedVrf] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
