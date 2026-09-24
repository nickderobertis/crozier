

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .engine_base_extension_thermic import EngineBaseExtensionThermic


class EngineBaseExtension(UniversalBaseModel):
    thermic: typing.Optional[EngineBaseExtensionThermic] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
