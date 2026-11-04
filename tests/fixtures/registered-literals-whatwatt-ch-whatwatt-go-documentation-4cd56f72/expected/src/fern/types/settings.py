

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .settings_services import SettingsServices
from .settings_system import SettingsSystem


class Settings(UniversalBaseModel):
    system: typing.Optional[SettingsSystem] = None
    services: typing.Optional[SettingsServices] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
