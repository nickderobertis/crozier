

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Item(UniversalBaseModel):
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
    allergy_type_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="allergyTypeId"), pydantic.Field(alias="allergyTypeId")
    ]
    description: str
    allergy_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="allergyType"), pydantic.Field(alias="allergyType")
    ]
    location_id: typing_extensions.Annotated[str, FieldMetadata(alias="locationId"), pydantic.Field(alias="locationId")]
    provider_id: typing_extensions.Annotated[str, FieldMetadata(alias="providerId"), pydantic.Field(alias="providerId")]
    onset_date: typing_extensions.Annotated[str, FieldMetadata(alias="onsetDate"), pydantic.Field(alias="onsetDate")]
    resolved_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="resolvedDate"), pydantic.Field(alias="resolvedDate")
    ]
    comment: str
    reaction_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="reactionDescription"), pydantic.Field(alias="reactionDescription")
    ]
    criticality_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="criticalityCode"), pydantic.Field(alias="criticalityCode")
    ]
    is_locked: typing_extensions.Annotated[str, FieldMetadata(alias="isLocked"), pydantic.Field(alias="isLocked")]
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
