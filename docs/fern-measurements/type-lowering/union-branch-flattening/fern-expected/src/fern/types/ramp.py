

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .common_ramp_properties import CommonRampProperties
from .fiat_source import FiatSource
from .ramp_direction import RampDirection


class Ramp(CommonRampProperties):
    """
    Referenced anyOf branches.
    """

    direction: typing.Optional[RampDirection] = None
    source: typing.Optional[FiatSource] = None
    destination: typing.Optional[str] = None
    payout: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
