

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .call_window import CallWindow
from .crew_unit import CrewUnit
from .gear_state import GearState


class CallSheetCrewResponse(UniversalBaseModel):
    call: typing.Optional[CallWindow] = None
    unit: typing.Optional[CrewUnit] = None
    gear: typing.Optional[typing.Dict[str, GearState]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
