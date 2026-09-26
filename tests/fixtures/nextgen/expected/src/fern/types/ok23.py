

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Ok23(UniversalBaseModel):
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    encounter_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterId"), pydantic.Field(alias="encounterId")
    ]
    enterprise_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="enterpriseId"), pydantic.Field(alias="enterpriseId")
    ]
    practice_id: typing_extensions.Annotated[str, FieldMetadata(alias="practiceId"), pydantic.Field(alias="practiceId")]
    is_deleted: typing_extensions.Annotated[str, FieldMetadata(alias="isDeleted"), pydantic.Field(alias="isDeleted")]
    goal_achieved: typing_extensions.Annotated[
        str, FieldMetadata(alias="goalAchieved"), pydantic.Field(alias="goalAchieved")
    ]
    goal_achieved_details: typing_extensions.Annotated[
        str, FieldMetadata(alias="goalAchievedDetails"), pydantic.Field(alias="goalAchievedDetails")
    ]
    goal_id: typing_extensions.Annotated[str, FieldMetadata(alias="goalId"), pydantic.Field(alias="goalId")]
    health_concern_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="healthConcernId"), pydantic.Field(alias="healthConcernId")
    ]
    intervention_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="interventionId"), pydantic.Field(alias="interventionId")
    ]
    description: str
    outcome_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="outcomeDate"), pydantic.Field(alias="outcomeDate")
    ]
    outcome_id: typing_extensions.Annotated[str, FieldMetadata(alias="OutcomeId"), pydantic.Field(alias="OutcomeId")]
    created_by: typing_extensions.Annotated[str, FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")]
    create_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="createTimestamp"), pydantic.Field(alias="createTimestamp")
    ]
    create_timestamp_time_zone: typing_extensions.Annotated[
        str, FieldMetadata(alias="createTimestampTimeZone"), pydantic.Field(alias="createTimestampTimeZone")
    ]
    modified_by: typing_extensions.Annotated[str, FieldMetadata(alias="modifiedBy"), pydantic.Field(alias="modifiedBy")]
    modify_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="modifyTimestamp"), pydantic.Field(alias="modifyTimestamp")
    ]
    modify_timestamp_time_zone: typing_extensions.Annotated[
        str, FieldMetadata(alias="modifyTimestampTimeZone"), pydantic.Field(alias="modifyTimestampTimeZone")
    ]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
