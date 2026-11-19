

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .firing_notes import FiringNotes
from .firing_summary import FiringSummary
from .glazing_step import GlazingStep
from .kiln_alarm_view import KilnAlarmView
from .kiln_plate import KilnPlate


class Bundle(UniversalBaseModel):
    glazing: typing.Optional[GlazingStep] = None
    summary: typing.Optional[FiringSummary] = None
    alarm: typing.Optional[KilnAlarmView] = None
    notes: typing.Optional[FiringNotes] = None
    plate: typing.Optional[KilnPlate] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
