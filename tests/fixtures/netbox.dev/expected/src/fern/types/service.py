

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_device import NestedDevice
from .nested_ip_address import NestedIpAddress
from .nested_tag import NestedTag
from .nested_virtual_machine import NestedVirtualMachine
from .service_protocol import ServiceProtocol


class Service(UniversalBaseModel):
    comments: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = None
    description: typing.Optional[str] = None
    device: typing.Optional[NestedDevice] = None
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    ipaddresses: typing.Optional[typing.List[NestedIpAddress]] = None
    last_updated: typing.Optional[dt.datetime] = None
    name: str
    ports: typing.List[int]
    protocol: typing.Optional[ServiceProtocol] = None
    tags: typing.Optional[typing.List[NestedTag]] = None
    url: typing.Optional[str] = None
    virtual_machine: typing.Optional[NestedVirtualMachine] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
