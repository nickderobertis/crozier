

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .device_airflow_label import DeviceAirflowLabel
from .device_airflow_value import DeviceAirflowValue


class DeviceAirflow(UniversalBaseModel):
    label: DeviceAirflowLabel
    value: DeviceAirflowValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
