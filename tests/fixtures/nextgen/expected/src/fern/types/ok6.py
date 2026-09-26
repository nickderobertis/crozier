

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Ok6(UniversalBaseModel):
    id: str
    patient_allergy_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="patientAllergyId"), pydantic.Field(alias="patientAllergyId")
    ]
    reaction_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="reactionDescription"), pydantic.Field(alias="reactionDescription")
    ]
    snomed_code: typing_extensions.Annotated[str, FieldMetadata(alias="snomedCode"), pydantic.Field(alias="snomedCode")]
    severity_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="severityCode"), pydantic.Field(alias="severityCode")
    ]
    severity_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="severityDescription"), pydantic.Field(alias="severityDescription")
    ]
    rank: str
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
