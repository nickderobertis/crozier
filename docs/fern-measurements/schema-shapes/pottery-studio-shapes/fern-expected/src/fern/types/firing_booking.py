

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .firing_booking_ending import FiringBookingEnding
from .firing_booking_shelf import FiringBookingShelf
from .target_cone import TargetCone


class FiringBooking(UniversalBaseModel):
    potter: str
    cone: TargetCone
    shelf: FiringBookingShelf
    ending: FiringBookingEnding
    palette: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
