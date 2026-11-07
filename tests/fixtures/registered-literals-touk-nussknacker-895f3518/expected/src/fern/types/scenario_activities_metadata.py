

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .scenario_activity_action_metadata import ScenarioActivityActionMetadata
from .scenario_activity_metadata import ScenarioActivityMetadata


class ScenarioActivitiesMetadata(UniversalBaseModel):
    activities: typing.Optional[typing.List[ScenarioActivityMetadata]] = None
    actions: typing.Optional[typing.List[ScenarioActivityActionMetadata]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
