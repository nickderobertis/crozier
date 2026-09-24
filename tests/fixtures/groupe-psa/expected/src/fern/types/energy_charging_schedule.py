

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .charge_schedule_program import ChargeScheduleProgram


class EnergyChargingSchedule(UniversalBaseModel):
    programs: typing.Optional[typing.List[ChargeScheduleProgram]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
