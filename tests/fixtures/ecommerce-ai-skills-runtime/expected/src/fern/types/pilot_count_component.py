

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pilot_count_component_status import PilotCountComponentStatus


class PilotCountComponent(UniversalBaseModel):
    required: bool
    status: PilotCountComponentStatus
    published_count: typing.Optional[int] = None
    enabled_schedule_count: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
