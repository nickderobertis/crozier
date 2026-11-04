

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_settings_response_services import GetSettingsResponseServices
from .get_settings_response_system import GetSettingsResponseSystem


class GetSettingsResponse(UniversalBaseModel):
    system: typing.Optional[GetSettingsResponseSystem] = None
    services: typing.Optional[GetSettingsResponseServices] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
