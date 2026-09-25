

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Item2(UniversalBaseModel):
    enterprise_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="enterpriseId"), pydantic.Field(alias="enterpriseId")
    ]
    practice_id: typing_extensions.Annotated[str, FieldMetadata(alias="practiceId"), pydantic.Field(alias="practiceId")]
    encounter_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterId"), pydantic.Field(alias="encounterId")
    ]
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    snomed_concept_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="snomedConceptId"), pydantic.Field(alias="snomedConceptId")
    ]
    date_onset: typing_extensions.Annotated[str, FieldMetadata(alias="dateOnset"), pydantic.Field(alias="dateOnset")]
    date_resolved: typing_extensions.Annotated[
        str, FieldMetadata(alias="dateResolved"), pydantic.Field(alias="dateResolved")
    ]
    allergy_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="allergyType"), pydantic.Field(alias="allergyType")
    ]
    encounter_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterTimestamp"), pydantic.Field(alias="encounterTimestamp")
    ]
    allergy_comment: typing_extensions.Annotated[
        str, FieldMetadata(alias="allergyComment"), pydantic.Field(alias="allergyComment")
    ]
    id: str
    category: str
    health_concern: typing_extensions.Annotated[
        str, FieldMetadata(alias="healthConcern"), pydantic.Field(alias="healthConcern")
    ]
    description: str
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
