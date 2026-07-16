

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_ip_address import NestedIpAddress
from .nested_tag import NestedTag
from .writable_ip_address_role import WritableIpAddressRole
from .writable_ip_address_status import WritableIpAddressStatus


class WritableIpAddress(UniversalBaseModel):
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

    family: typing.Optional[str] = None
    id: typing.Optional[int] = None
    last_updated: typing.Optional[dt.datetime] = None
    nat_inside: typing.Optional[int] = pydantic.Field(default=None)
    """
    The IP for which this address is the "outside" IP
    """

    nat_outside: typing.Optional[typing.List[NestedIpAddress]] = None
    role: typing.Optional[WritableIpAddressRole] = pydantic.Field(default=None)
    """
    The functional role of this IP
    """

    status: typing.Optional[WritableIpAddressStatus] = pydantic.Field(default=None)
    """
    The operational status of this IP
    """

    tags: typing.Optional[typing.List[NestedTag]] = None
    tenant: typing.Optional[int] = None
    url: typing.Optional[str] = None
    vrf: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
