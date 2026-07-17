

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .device_airflow import DeviceAirflow
from .device_face import DeviceFace
from .device_status import DeviceStatus
from .nested_cluster import NestedCluster
from .nested_device import NestedDevice
from .nested_device_role import NestedDeviceRole
from .nested_device_type import NestedDeviceType
from .nested_ip_address import NestedIpAddress
from .nested_location import NestedLocation
from .nested_platform import NestedPlatform
from .nested_rack import NestedRack
from .nested_site import NestedSite
from .nested_tag import NestedTag
from .nested_tenant import NestedTenant
from .nested_virtual_chassis import NestedVirtualChassis


class Device(UniversalBaseModel):
    airflow: typing.Optional[DeviceAirflow] = None
    asset_tag: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique tag used to identify this device
    """

    cluster: typing.Optional[NestedCluster] = None
    comments: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = None
    description: typing.Optional[str] = None
    device_role: NestedDeviceRole
    device_type: NestedDeviceType
    display: typing.Optional[str] = None
    face: typing.Optional[DeviceFace] = None
    id: typing.Optional[int] = None
    last_updated: typing.Optional[dt.datetime] = None
    local_context_data: typing.Optional[typing.Dict[str, typing.Any]] = None
    location: typing.Optional[NestedLocation] = None
    name: typing.Optional[str] = None
    parent_device: typing.Optional[NestedDevice] = None
    platform: typing.Optional[NestedPlatform] = None
    position: typing.Optional[float] = None
    primary_ip: typing.Optional[NestedIpAddress] = None
    primary_ip4: typing.Optional[NestedIpAddress] = None
    primary_ip6: typing.Optional[NestedIpAddress] = None
    rack: typing.Optional[NestedRack] = None
    serial: typing.Optional[str] = None
    site: typing.Optional[NestedSite] = None
    status: typing.Optional[DeviceStatus] = None
    tags: typing.Optional[typing.List[NestedTag]] = None
    tenant: typing.Optional[NestedTenant] = None
    url: typing.Optional[str] = None
    vc_position: typing.Optional[int] = None
    vc_priority: typing.Optional[int] = None
    virtual_chassis: typing.Optional[NestedVirtualChassis] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
