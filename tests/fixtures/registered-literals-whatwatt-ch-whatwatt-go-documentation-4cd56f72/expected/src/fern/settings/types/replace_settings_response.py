

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .replace_settings_response_services import ReplaceSettingsResponseServices
from .replace_settings_response_system import ReplaceSettingsResponseSystem


class ReplaceSettingsResponse(UniversalBaseModel):
    system: typing.Optional[ReplaceSettingsResponseSystem] = None
    services: typing.Optional[ReplaceSettingsResponseServices] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
