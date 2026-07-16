

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_tag import NestedTag
from .writable_site_status import WritableSiteStatus


class WritableSite(UniversalBaseModel):
    asns: typing.Optional[typing.List[int]] = None
    circuit_count: typing.Optional[int] = None
    comments: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    description: typing.Optional[str] = None
    device_count: typing.Optional[int] = None
    display: typing.Optional[str] = None
    facility: typing.Optional[str] = pydantic.Field(default=None)
    """
    Local facility ID or description
    """

    group: typing.Optional[int] = None
    id: typing.Optional[int] = None
    last_updated: typing.Optional[dt.datetime] = None
    latitude: typing.Optional[float] = pydantic.Field(default=None)
    """
    GPS coordinate (latitude)
    """

    longitude: typing.Optional[float] = pydantic.Field(default=None)
    """
    GPS coordinate (longitude)
    """

    name: str
    physical_address: typing.Optional[str] = None
    prefix_count: typing.Optional[int] = None
    rack_count: typing.Optional[int] = None
    region: typing.Optional[int] = None
    shipping_address: typing.Optional[str] = None
    slug: str
    status: typing.Optional[WritableSiteStatus] = None
    tags: typing.Optional[typing.List[NestedTag]] = None
    tenant: typing.Optional[int] = None
    time_zone: typing.Optional[str] = None
    url: typing.Optional[str] = None
    virtualmachine_count: typing.Optional[int] = None
    vlan_count: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
