

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nine_thousand_nine_hundred_ninety_nine_stock import NineThousandNineHundredNinetyNineStock
from .one_hundred_ten_crew import OneHundredTenCrew
from .one_thousand_cone import OneThousandCone
from .one_thousand_two_hundred_thirty_four_plan import OneThousandTwoHundredThirtyFourPlan
from .seven_agent import SevenAgent
from .twenty_one_club import TwentyOneClub
from .two_fa_status import TwoFaStatus
from .undefined_bricks import UndefinedBricks
from .undefined_pixels import UndefinedPixels
from .undefined_seats import UndefinedSeats
from .undefined_steps import UndefinedSteps
from .undefined_viewers import UndefinedViewers


class TwelveHourCycle(UniversalBaseModel):
    peak: typing.Optional[int] = None
    cone: typing.Optional[OneThousandCone] = None
    agent: typing.Optional[SevenAgent] = None
    club: typing.Optional[TwentyOneClub] = None
    plan: typing.Optional[OneThousandTwoHundredThirtyFourPlan] = None
    audience: typing.Optional[UndefinedViewers] = None
    security: typing.Optional[TwoFaStatus] = None
    seats: typing.Optional[UndefinedSeats] = None
    pixels: typing.Optional[UndefinedPixels] = None
    crew: typing.Optional[OneHundredTenCrew] = None
    stock: typing.Optional[NineThousandNineHundredNinetyNineStock] = None
    steps: typing.Optional[UndefinedSteps] = None
    bricks: typing.Optional[UndefinedBricks] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
