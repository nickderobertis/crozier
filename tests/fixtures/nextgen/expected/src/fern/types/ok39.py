

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Ok39(UniversalBaseModel):
    id: str
    enterprise_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="enterpriseId"), pydantic.Field(alias="enterpriseId")
    ]
    practice_id: typing_extensions.Annotated[str, FieldMetadata(alias="practiceId"), pydantic.Field(alias="practiceId")]
    encounter_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterId"), pydantic.Field(alias="encounterId")
    ]
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    person_name: typing_extensions.Annotated[str, FieldMetadata(alias="personName"), pydantic.Field(alias="personName")]
    user_friendly_order_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="userFriendlyOrderNumber"), pydantic.Field(alias="userFriendlyOrderNumber")
    ]
    generated_by: typing_extensions.Annotated[
        str, FieldMetadata(alias="generatedBy"), pydantic.Field(alias="generatedBy")
    ]
    location_id: typing_extensions.Annotated[str, FieldMetadata(alias="locationId"), pydantic.Field(alias="locationId")]
    location_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="locationName"), pydantic.Field(alias="locationName")
    ]
    ordering_provider_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="orderingProviderId"), pydantic.Field(alias="orderingProviderId")
    ]
    ordering_provider_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="orderingProviderName"), pydantic.Field(alias="orderingProviderName")
    ]
    supervisor_provider_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="supervisorProviderId"), pydantic.Field(alias="supervisorProviderId")
    ]
    status: str
    vaccine_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="vaccineDescription"), pydantic.Field(alias="vaccineDescription")
    ]
    create_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="createTimestamp"), pydantic.Field(alias="createTimestamp")
    ]
    create_timestamp_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="createTimestampTimezone"), pydantic.Field(alias="createTimestampTimezone")
    ]
    modify_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="modifyTimestamp"), pydantic.Field(alias="modifyTimestamp")
    ]
    modify_timestamp_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="modifyTimestampTimezone"), pydantic.Field(alias="modifyTimestampTimezone")
    ]
    registry_id: typing_extensions.Annotated[str, FieldMetadata(alias="registryId"), pydantic.Field(alias="registryId")]
    interface_message: typing_extensions.Annotated[
        str, FieldMetadata(alias="interfaceMessage"), pydantic.Field(alias="interfaceMessage")
    ]
    has_documents: typing_extensions.Annotated[
        str, FieldMetadata(alias="hasDocuments"), pydantic.Field(alias="hasDocuments")
    ]
    has_tracking_comments: typing_extensions.Annotated[
        str, FieldMetadata(alias="hasTrackingComments"), pydantic.Field(alias="hasTrackingComments")
    ]
    immunizations_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="immunizationsDescription"), pydantic.Field(alias="immunizationsDescription")
    ]
    order_comment: typing_extensions.Annotated[
        str, FieldMetadata(alias="orderComment"), pydantic.Field(alias="orderComment")
    ]
    is_verbal_order: typing_extensions.Annotated[
        str, FieldMetadata(alias="isVerbalOrder"), pydantic.Field(alias="isVerbalOrder")
    ]
    allergies_reviewed: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="allergiesReviewed"), pydantic.Field(alias="allergiesReviewed")
    ]
    cancel_reason: typing_extensions.Annotated[
        str, FieldMetadata(alias="cancelReason"), pydantic.Field(alias="cancelReason")
    ]
    sign_off_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="signOffDate"), pydantic.Field(alias="signOffDate")
    ]
    sign_off_date_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="signOffDateTimezone"), pydantic.Field(alias="signOffDateTimezone")
    ]
    sign_off_user_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="signOffUserId"), pydantic.Field(alias="signOffUserId")
    ]
    sign_off_user_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="signOffUserName"), pydantic.Field(alias="signOffUserName")
    ]
    privacy_level: typing_extensions.Annotated[
        str, FieldMetadata(alias="privacyLevel"), pydantic.Field(alias="privacyLevel")
    ]
    encounter_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterTimestamp"), pydantic.Field(alias="encounterTimestamp")
    ]
    encounter_timestamp_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterTimestampTimezone"), pydantic.Field(alias="encounterTimestampTimezone")
    ]
    is_deleted: typing_extensions.Annotated[str, FieldMetadata(alias="isDeleted"), pydantic.Field(alias="isDeleted")]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
