

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .plan_activities_value import PlanActivitiesValue


class Plan(UniversalBaseModel):
    id: str
    activities: typing.Optional[typing.Dict[str, typing.Optional[PlanActivitiesValue]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
