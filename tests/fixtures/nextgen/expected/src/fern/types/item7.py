

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Item7(UniversalBaseModel):
    goal_id: typing_extensions.Annotated[str, FieldMetadata(alias="goalId"), pydantic.Field(alias="goalId")]
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    encounter_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterId"), pydantic.Field(alias="encounterId")
    ]
    health_concern_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="healthConcernId"), pydantic.Field(alias="healthConcernId")
    ]
    code_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="codeDescription"), pydantic.Field(alias="codeDescription")
    ]
    code_system: typing_extensions.Annotated[str, FieldMetadata(alias="codeSystem"), pydantic.Field(alias="codeSystem")]
    code_value: typing_extensions.Annotated[str, FieldMetadata(alias="codeValue"), pydantic.Field(alias="codeValue")]
    comments: str
    is_deleted: typing_extensions.Annotated[str, FieldMetadata(alias="isDeleted"), pydantic.Field(alias="isDeleted")]
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
    documented_by: typing_extensions.Annotated[
        str, FieldMetadata(alias="documentedBy"), pydantic.Field(alias="documentedBy")
    ]
    encounter_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterDate"), pydantic.Field(alias="encounterDate")
    ]
    sequence_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="sequenceNumber"), pydantic.Field(alias="sequenceNumber")
    ]
    created_by: typing_extensions.Annotated[str, FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")]
    create_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="createTimestamp"), pydantic.Field(alias="createTimestamp")
    ]
    modified_by: typing_extensions.Annotated[str, FieldMetadata(alias="modifiedBy"), pydantic.Field(alias="modifiedBy")]
    modify_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="modifyTimestamp"), pydantic.Field(alias="modifyTimestamp")
    ]
    create_timestamp_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="createTimestampTimezone"), pydantic.Field(alias="createTimestampTimezone")
    ]
    modify_timestamp_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="modifyTimestampTimezone"), pydantic.Field(alias="modifyTimestampTimezone")
    ]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
