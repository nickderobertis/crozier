

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BaseUrlPersonsPersonIdChartEncountersEncounterIdAllergiesRequest(UniversalBaseModel):
    allergy_id: typing_extensions.Annotated[str, FieldMetadata(alias="allergyId"), pydantic.Field(alias="allergyId")]
    allergy_type_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="allergyTypeId"), pydantic.Field(alias="allergyTypeId")
    ]
    onset_date: typing_extensions.Annotated[str, FieldMetadata(alias="onsetDate"), pydantic.Field(alias="onsetDate")]
    resolved_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="resolvedDate"), pydantic.Field(alias="resolvedDate")
    ]
    comment: str
    provider_id: typing_extensions.Annotated[str, FieldMetadata(alias="providerId"), pydantic.Field(alias="providerId")]
    location_id: typing_extensions.Annotated[str, FieldMetadata(alias="locationId"), pydantic.Field(alias="locationId")]
    is_intolerant: typing_extensions.Annotated[
        str, FieldMetadata(alias="isIntolerant"), pydantic.Field(alias="isIntolerant")
    ]
    is_recorded_elsewhere: typing_extensions.Annotated[
        str, FieldMetadata(alias="isRecordedElsewhere"), pydantic.Field(alias="isRecordedElsewhere")
    ]
    recorded_elsewhere_source: typing_extensions.Annotated[
        str, FieldMetadata(alias="recordedElsewhereSource"), pydantic.Field(alias="recordedElsewhereSource")
    ]
    allow_duplicate_allergies: typing_extensions.Annotated[
        str, FieldMetadata(alias="allowDuplicateAllergies"), pydantic.Field(alias="allowDuplicateAllergies")
    ]
    no_known_allergies: typing_extensions.Annotated[
        str, FieldMetadata(alias="noKnownAllergies"), pydantic.Field(alias="noKnownAllergies")
    ]
    criticality_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="criticalityCode"), pydantic.Field(alias="criticalityCode")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
