

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .fiat_source import FiatSource
from .on_ramp_properties_direction import OnRampPropertiesDirection


class OnRampProperties(UniversalBaseModel):
    direction: OnRampPropertiesDirection
    source: FiatSource
    destination: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
