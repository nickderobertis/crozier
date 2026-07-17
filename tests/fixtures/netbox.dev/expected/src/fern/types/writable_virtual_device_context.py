

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_tag import NestedTag
from .writable_virtual_device_context_status import WritableVirtualDeviceContextStatus


class WritableVirtualDeviceContext(UniversalBaseModel):
    comments: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = None
    description: typing.Optional[str] = None
    device: typing.Optional[int] = None
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    identifier: typing.Optional[int] = pydantic.Field(default=None)
    """
    Numeric identifier unique to the parent device
    """

    interface_count: typing.Optional[int] = None
    last_updated: typing.Optional[dt.datetime] = None
    name: str
    primary_ip: typing.Optional[str] = None
    primary_ip4: typing.Optional[int] = None
    primary_ip6: typing.Optional[int] = None
    status: WritableVirtualDeviceContextStatus
    tags: typing.Optional[typing.List[NestedTag]] = None
    tenant: typing.Optional[int] = None
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
