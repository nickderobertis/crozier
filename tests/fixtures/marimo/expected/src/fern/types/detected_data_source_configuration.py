

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .detected_data_source_configuration_value import DetectedDataSourceConfigurationValue


class DetectedDataSourceConfiguration(UniversalBaseModel):
    field: str
    value: DetectedDataSourceConfigurationValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
