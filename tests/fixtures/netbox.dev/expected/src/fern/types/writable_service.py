

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_tag import NestedTag
from .writable_service_protocol import WritableServiceProtocol


class WritableService(UniversalBaseModel):
    comments: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = None
    description: typing.Optional[str] = None
    device: typing.Optional[int] = None
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    ipaddresses: typing.Optional[typing.List[int]] = None
    last_updated: typing.Optional[dt.datetime] = None
    name: str
    ports: typing.List[int]
    protocol: WritableServiceProtocol
    tags: typing.Optional[typing.List[NestedTag]] = None
    url: typing.Optional[str] = None
    virtual_machine: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
