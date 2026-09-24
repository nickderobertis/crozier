

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .engine_air import EngineAir
from .engine_base_extension_thermic_coolant import EngineBaseExtensionThermicCoolant
from .engine_base_extension_thermic_oil import EngineBaseExtensionThermicOil


class EngineBaseExtensionThermic(UniversalBaseModel):
    coolant: typing.Optional[EngineBaseExtensionThermicCoolant] = pydantic.Field(default=None)
    """
    Engine coolant liquid properties.
    """

    oil: typing.Optional[EngineBaseExtensionThermicOil] = pydantic.Field(default=None)
    """
    Engine oil properties.
    """

    air: typing.Optional[EngineAir] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
