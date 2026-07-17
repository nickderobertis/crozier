

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .device_type_airflow import DeviceTypeAirflow
from .device_type_subdevice_role import DeviceTypeSubdeviceRole
from .device_type_weight_unit import DeviceTypeWeightUnit
from .nested_manufacturer import NestedManufacturer
from .nested_tag import NestedTag


class DeviceType(UniversalBaseModel):
    airflow: typing.Optional[DeviceTypeAirflow] = None
    comments: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = None
    description: typing.Optional[str] = None
    device_count: typing.Optional[int] = None
    display: typing.Optional[str] = None
    front_image: typing.Optional[str] = None
    id: typing.Optional[int] = None
    is_full_depth: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Device consumes both front and rear rack faces
    """

    last_updated: typing.Optional[dt.datetime] = None
    manufacturer: NestedManufacturer
    model: str
    part_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    Discrete part number (optional)
    """

    rear_image: typing.Optional[str] = None
    slug: str
    subdevice_role: typing.Optional[DeviceTypeSubdeviceRole] = None
    tags: typing.Optional[typing.List[NestedTag]] = None
    u_height: typing.Optional[float] = None
    url: typing.Optional[str] = None
    weight: typing.Optional[float] = None
    weight_unit: typing.Optional[DeviceTypeWeightUnit] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
