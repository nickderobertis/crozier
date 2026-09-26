

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BaseUrlPersonsPersonIdChartEncountersEncounterIdCarePlanHealthConcernsHealthConcernIdGoalsGoalIdRequest(
    UniversalBaseModel
):
    code_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="codeDescription"), pydantic.Field(alias="codeDescription")
    ]
    code_system: typing_extensions.Annotated[str, FieldMetadata(alias="codeSystem"), pydantic.Field(alias="codeSystem")]
    code_value: typing_extensions.Annotated[str, FieldMetadata(alias="codeValue"), pydantic.Field(alias="codeValue")]
    comments: str
    description: str
    is_goal_achieved: typing_extensions.Annotated[
        str, FieldMetadata(alias="isGoalAchieved"), pydantic.Field(alias="isGoalAchieved")
    ]
    goal_achieved_details: typing_extensions.Annotated[
        str, FieldMetadata(alias="goalAchievedDetails"), pydantic.Field(alias="goalAchievedDetails")
    ]
    goal_completion_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="goalCompletionDate"), pydantic.Field(alias="goalCompletionDate")
    ]
    goal_start_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="goalStartDate"), pydantic.Field(alias="goalStartDate")
    ]
    is_patient_goal: typing_extensions.Annotated[
        str, FieldMetadata(alias="isPatientGoal"), pydantic.Field(alias="isPatientGoal")
    ]
    patient_priority: typing_extensions.Annotated[
        str, FieldMetadata(alias="patientPriority"), pydantic.Field(alias="patientPriority")
    ]
    is_provider_goal: typing_extensions.Annotated[
        str, FieldMetadata(alias="isProviderGoal"), pydantic.Field(alias="isProviderGoal")
    ]
    provider_priority: typing_extensions.Annotated[
        str, FieldMetadata(alias="providerPriority"), pydantic.Field(alias="providerPriority")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
