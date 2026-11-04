

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_settings_response_services import UpdateSettingsResponseServices
from .update_settings_response_system import UpdateSettingsResponseSystem


class UpdateSettingsResponse(UniversalBaseModel):
    system: typing.Optional[UpdateSettingsResponseSystem] = None
    services: typing.Optional[UpdateSettingsResponseServices] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
