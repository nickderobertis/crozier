

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_cluster import NestedCluster
from .nested_device import NestedDevice
from .nested_device_role import NestedDeviceRole
from .nested_ip_address import NestedIpAddress
from .nested_platform import NestedPlatform
from .nested_site import NestedSite
from .nested_tag import NestedTag
from .nested_tenant import NestedTenant
from .virtual_machine_with_config_context_status import VirtualMachineWithConfigContextStatus


class VirtualMachineWithConfigContext(UniversalBaseModel):
    cluster: typing.Optional[NestedCluster] = None
    comments: typing.Optional[str] = None
    config_context: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    description: typing.Optional[str] = None
    device: typing.Optional[NestedDevice] = None
    disk: typing.Optional[int] = None
    display: typing.Optional[str] = None
    id: typing.Optional[int] = None
    last_updated: typing.Optional[dt.datetime] = None
    local_context_data: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    memory: typing.Optional[int] = None
    name: str
    platform: typing.Optional[NestedPlatform] = None
    primary_ip: typing.Optional[NestedIpAddress] = None
    primary_ip4: typing.Optional[NestedIpAddress] = None
    primary_ip6: typing.Optional[NestedIpAddress] = None
    role: typing.Optional[NestedDeviceRole] = None
    site: typing.Optional[NestedSite] = None
    status: typing.Optional[VirtualMachineWithConfigContextStatus] = None
    tags: typing.Optional[typing.List[NestedTag]] = None
    tenant: typing.Optional[NestedTenant] = None
    url: typing.Optional[str] = None
    vcpus: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
