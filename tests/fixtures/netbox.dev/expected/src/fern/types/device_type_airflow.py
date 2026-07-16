

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .device_type_airflow_label import DeviceTypeAirflowLabel
from .device_type_airflow_value import DeviceTypeAirflowValue


class DeviceTypeAirflow(UniversalBaseModel):
    label: DeviceTypeAirflowLabel
    value: DeviceTypeAirflowValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
