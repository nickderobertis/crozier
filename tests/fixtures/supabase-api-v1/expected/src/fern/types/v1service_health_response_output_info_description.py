

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1service_health_response_output_info_description_name import V1ServiceHealthResponseOutputInfoDescriptionName


class V1ServiceHealthResponseOutputInfoDescription(UniversalBaseModel):
    name: V1ServiceHealthResponseOutputInfoDescriptionName
    version: str
    description: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
