

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transmission_gearbox_mode import TransmissionGearboxMode
from .transmission_gearbox_ratio import TransmissionGearboxRatio


class TransmissionGearbox(UniversalBaseModel):
    mode: typing.Optional[TransmissionGearboxMode] = None
    ratio: typing.Optional[TransmissionGearboxRatio] = pydantic.Field(default=None)
    """
    Current gear-box ratio.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
