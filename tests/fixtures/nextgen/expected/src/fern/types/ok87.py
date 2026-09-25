

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Ok87(UniversalBaseModel):
    id: str
    enterprise_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="enterpriseId"), pydantic.Field(alias="enterpriseId")
    ]
    practice_id: typing_extensions.Annotated[str, FieldMetadata(alias="practiceId"), pydantic.Field(alias="practiceId")]
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    description: str
    fully_specified_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="fullySpecifiedName"), pydantic.Field(alias="fullySpecifiedName")
    ]
    concept_id: typing_extensions.Annotated[str, FieldMetadata(alias="conceptId"), pydantic.Field(alias="conceptId")]
    side_id: typing_extensions.Annotated[str, FieldMetadata(alias="sideId"), pydantic.Field(alias="sideId")]
    site: str
    onset_date: typing_extensions.Annotated[str, FieldMetadata(alias="onsetDate"), pydantic.Field(alias="onsetDate")]
    last_addressed_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="lastAddressedDate"), pydantic.Field(alias="lastAddressedDate")
    ]
    resolved_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="resolvedDate"), pydantic.Field(alias="resolvedDate")
    ]
    resolved_reason: typing_extensions.Annotated[
        str, FieldMetadata(alias="resolvedReason"), pydantic.Field(alias="resolvedReason")
    ]
    resolved_by: typing_extensions.Annotated[str, FieldMetadata(alias="resolvedBy"), pydantic.Field(alias="resolvedBy")]
    problem_status_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="problemStatusId"), pydantic.Field(alias="problemStatusId")
    ]
    problem_status: typing_extensions.Annotated[
        str, FieldMetadata(alias="problemStatus"), pydantic.Field(alias="problemStatus")
    ]
    recent_note_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="recentNoteId"), pydantic.Field(alias="recentNoteId")
    ]
    clinical_status_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="clinicalStatusId"), pydantic.Field(alias="clinicalStatusId")
    ]
    is_chronic: typing_extensions.Annotated[str, FieldMetadata(alias="isChronic"), pydantic.Field(alias="isChronic")]
    has_secondary_condition: typing_extensions.Annotated[
        str, FieldMetadata(alias="hasSecondaryCondition"), pydantic.Field(alias="hasSecondaryCondition")
    ]
    is_deleted: typing_extensions.Annotated[str, FieldMetadata(alias="isDeleted"), pydantic.Field(alias="isDeleted")]
    location_id: typing_extensions.Annotated[str, FieldMetadata(alias="locationId"), pydantic.Field(alias="locationId")]
    provider_id: typing_extensions.Annotated[str, FieldMetadata(alias="providerId"), pydantic.Field(alias="providerId")]
    is_recorded_elsewhere: typing_extensions.Annotated[
        str, FieldMetadata(alias="isRecordedElsewhere"), pydantic.Field(alias="isRecordedElsewhere")
    ]
    recorded_elsewhere_source: typing_extensions.Annotated[
        str, FieldMetadata(alias="recordedElsewhereSource"), pydantic.Field(alias="recordedElsewhereSource")
    ]
    responsible_provider_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="responsibleProviderId"), pydantic.Field(alias="responsibleProviderId")
    ]
    is_comorbid: typing_extensions.Annotated[str, FieldMetadata(alias="isComorbid"), pydantic.Field(alias="isComorbid")]
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
