

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BaseUrlPersonsPersonIdChartEncountersEncounterIdCarePlanHealthConcernsHealthConcernIdGoalsGoalIdInterventionsInterventionIdOutcomesRequest(
    UniversalBaseModel
):
    outcome: str
    goal_achieved: typing_extensions.Annotated[
        str, FieldMetadata(alias="goalAchieved"), pydantic.Field(alias="goalAchieved")
    ]
    goal_achieved_details: typing_extensions.Annotated[
        str, FieldMetadata(alias="goalAchievedDetails"), pydantic.Field(alias="goalAchievedDetails")
    ]
    outcome_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="outcomeDate"), pydantic.Field(alias="outcomeDate")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
