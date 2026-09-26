

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .air_base import AirBase
from .luminosity_base import LuminosityBase


class EnvironmentBase(UniversalBaseModel):
    luminosity: typing.Optional[LuminosityBase] = None
    air: typing.Optional[AirBase] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
