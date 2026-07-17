

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ip_range_family import IpRangeFamily
from .ip_range_status import IpRangeStatus
from .nested_role import NestedRole
from .nested_tag import NestedTag
from .nested_tenant import NestedTenant
from .nested_vrf import NestedVrf


class IpRange(UniversalBaseModel):
    children: typing.Optional[int] = None
    comments: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = None
    description: typing.Optional[str] = None
    display: typing.Optional[str] = None
    end_address: str = pydantic.Field()
    """
    IPv4 or IPv6 address (with mask)
    """

    family: typing.Optional[IpRangeFamily] = None
    id: typing.Optional[int] = None
    last_updated: typing.Optional[dt.datetime] = None
    role: typing.Optional[NestedRole] = None
    size: typing.Optional[int] = None
    start_address: str = pydantic.Field()
    """
    IPv4 or IPv6 address (with mask)
    """

    status: typing.Optional[IpRangeStatus] = None
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
