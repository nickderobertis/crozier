

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .device_with_config_context_airflow_label import DeviceWithConfigContextAirflowLabel
from .device_with_config_context_airflow_value import DeviceWithConfigContextAirflowValue


class DeviceWithConfigContextAirflow(UniversalBaseModel):
    label: DeviceWithConfigContextAirflowLabel
    value: DeviceWithConfigContextAirflowValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
