

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chain_source import ChainSource
from .off_ramp_properties_direction import OffRampPropertiesDirection


class OffRampProperties(UniversalBaseModel):
    direction: OffRampPropertiesDirection
    source: ChainSource
    payout: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
