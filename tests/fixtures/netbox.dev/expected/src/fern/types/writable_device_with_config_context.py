

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nested_device import NestedDevice
from .nested_tag import NestedTag
from .writable_device_with_config_context_airflow import WritableDeviceWithConfigContextAirflow
from .writable_device_with_config_context_face import WritableDeviceWithConfigContextFace
from .writable_device_with_config_context_status import WritableDeviceWithConfigContextStatus


class WritableDeviceWithConfigContext(UniversalBaseModel):
    airflow: typing.Optional[WritableDeviceWithConfigContextAirflow] = None
    asset_tag: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique tag used to identify this device
    """

    cluster: typing.Optional[int] = None
    comments: typing.Optional[str] = None
    config_context: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    description: typing.Optional[str] = None
    device_role: int
    device_type: int
    display: typing.Optional[str] = None
    face: typing.Optional[WritableDeviceWithConfigContextFace] = None
    id: typing.Optional[int] = None
    last_updated: typing.Optional[dt.datetime] = None
    local_context_data: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    location: typing.Optional[int] = None
    name: typing.Optional[str] = None
    parent_device: typing.Optional[NestedDevice] = None
    platform: typing.Optional[int] = None
    position: typing.Optional[float] = None
    primary_ip: typing.Optional[str] = None
    primary_ip4: typing.Optional[int] = None
    primary_ip6: typing.Optional[int] = None
    rack: typing.Optional[int] = None
    serial: typing.Optional[str] = None
    site: int
    status: typing.Optional[WritableDeviceWithConfigContextStatus] = None
    tags: typing.Optional[typing.List[NestedTag]] = None
    tenant: typing.Optional[int] = None
    url: typing.Optional[str] = None
    vc_position: typing.Optional[int] = None
    vc_priority: typing.Optional[int] = None
    virtual_chassis: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
