

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Ok1(UniversalBaseModel):
    id: str
    enterprise_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="enterpriseId"), pydantic.Field(alias="enterpriseId")
    ]
    practice_id: typing_extensions.Annotated[str, FieldMetadata(alias="practiceId"), pydantic.Field(alias="practiceId")]
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    encounter_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterId"), pydantic.Field(alias="encounterId")
    ]
    encounter_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterTimestamp"), pydantic.Field(alias="encounterTimestamp")
    ]
    encounter_timestamp_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterTimestampTimezone"), pydantic.Field(alias="encounterTimestampTimezone")
    ]
    allergy_id: typing_extensions.Annotated[str, FieldMetadata(alias="allergyId"), pydantic.Field(alias="allergyId")]
    allergy_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="allergyType"), pydantic.Field(alias="allergyType")
    ]
    allergy_type_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="allergyTypeId"), pydantic.Field(alias="allergyTypeId")
    ]
    location_id: typing_extensions.Annotated[str, FieldMetadata(alias="locationId"), pydantic.Field(alias="locationId")]
    location_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="locationName"), pydantic.Field(alias="locationName")
    ]
    provider_id: typing_extensions.Annotated[str, FieldMetadata(alias="providerId"), pydantic.Field(alias="providerId")]
    provider_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="providerName"), pydantic.Field(alias="providerName")
    ]
    onset_date: typing_extensions.Annotated[str, FieldMetadata(alias="onsetDate"), pydantic.Field(alias="onsetDate")]
    resolved_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="resolvedDate"), pydantic.Field(alias="resolvedDate")
    ]
    comment: str
    reaction_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="reactionDescription"), pydantic.Field(alias="reactionDescription")
    ]
    source_product_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="sourceProductId"), pydantic.Field(alias="sourceProductId")
    ]
    audit_id: typing_extensions.Annotated[str, FieldMetadata(alias="auditId"), pydantic.Field(alias="auditId")]
    causative_agent: typing_extensions.Annotated[
        str, FieldMetadata(alias="causativeAgent"), pydantic.Field(alias="causativeAgent")
    ]
    who_reviewed: typing_extensions.Annotated[
        str, FieldMetadata(alias="whoReviewed"), pydantic.Field(alias="whoReviewed")
    ]
    when_reviewed: typing_extensions.Annotated[
        str, FieldMetadata(alias="whenReviewed"), pydantic.Field(alias="whenReviewed")
    ]
    is_locked: typing_extensions.Annotated[str, FieldMetadata(alias="isLocked"), pydantic.Field(alias="isLocked")]
    severity_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="severityCode"), pydantic.Field(alias="severityCode")
    ]
    is_intolerant: typing_extensions.Annotated[
        str, FieldMetadata(alias="isIntolerant"), pydantic.Field(alias="isIntolerant")
    ]
    description: str
    criticality_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="criticalityCode"), pydantic.Field(alias="criticalityCode")
    ]
    created_by: typing_extensions.Annotated[str, FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")]
    create_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="createTimestamp"), pydantic.Field(alias="createTimestamp")
    ]
    create_timestamp_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="createTimestampTimezone"), pydantic.Field(alias="createTimestampTimezone")
    ]
    modified_by: typing_extensions.Annotated[str, FieldMetadata(alias="modifiedBy"), pydantic.Field(alias="modifiedBy")]
    modify_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="modifyTimestamp"), pydantic.Field(alias="modifyTimestamp")
    ]
    modify_timestamp_timezone: typing_extensions.Annotated[
        str, FieldMetadata(alias="modifyTimestampTimezone"), pydantic.Field(alias="modifyTimestampTimezone")
    ]
    is_read_only: typing_extensions.Annotated[
        str, FieldMetadata(alias="isReadOnly"), pydantic.Field(alias="isReadOnly")
    ]
    rx_norm_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="rxNormCode"), pydantic.Field(alias="rxNormCode")
    ]
    rx_norm_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="rxNormDescription"), pydantic.Field(alias="rxNormDescription")
    ]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
