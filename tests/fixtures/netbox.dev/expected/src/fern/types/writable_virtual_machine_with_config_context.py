

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_tag import NestedTag
from .writable_virtual_machine_with_config_context_status import WritableVirtualMachineWithConfigContextStatus


class WritableVirtualMachineWithConfigContext(UniversalBaseModel):
    cluster: typing.Optional[int] = None
    comments: typing.Optional[str] = None
    config_context: typing.Optional[typing.Dict[str, typing.Any]] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = None
    description: typing.Optional[str] = None
    device: typing.Optional[int] = None
    disk: typing.Optional[int] = None
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    last_updated: typing.Optional[dt.datetime] = None
    local_context_data: typing.Optional[typing.Dict[str, typing.Any]] = None
    memory: typing.Optional[int] = None
    name: str
    platform: typing.Optional[int] = None
    primary_ip: typing.Optional[str] = None
    primary_ip4: typing.Optional[int] = None
    primary_ip6: typing.Optional[int] = None
    role: typing.Optional[int] = None
    site: typing.Optional[int] = None
    status: typing.Optional[WritableVirtualMachineWithConfigContextStatus] = None
    tags: typing.Optional[typing.List[NestedTag]] = None
    tenant: typing.Optional[int] = None
    url: typing.Optional[str] = None
    vcpus: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
