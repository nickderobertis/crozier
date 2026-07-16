

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_tag import NestedTag
from .writable_ip_range_status import WritableIpRangeStatus


class WritableIpRange(UniversalBaseModel):
    children: typing.Optional[int] = None
    comments: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    description: typing.Optional[str] = None
    display: typing.Optional[str] = None
    end_address: str = pydantic.Field()
    """
    IPv4 or IPv6 address (with mask)
    """

    family: typing.Optional[str] = None
    id: typing.Optional[int] = None
    last_updated: typing.Optional[dt.datetime] = None
    role: typing.Optional[int] = pydantic.Field(default=None)
    """
    The primary function of this range
    """

    size: typing.Optional[int] = None
    start_address: str = pydantic.Field()
    """
    IPv4 or IPv6 address (with mask)
    """

    status: typing.Optional[WritableIpRangeStatus] = pydantic.Field(default=None)
    """
    Operational status of this range
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
