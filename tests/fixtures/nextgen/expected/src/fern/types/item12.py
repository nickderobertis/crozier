

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Item12(UniversalBaseModel):
    encounter_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterDate"), pydantic.Field(alias="encounterDate")
    ]
    description: str
    icd_code: typing_extensions.Annotated[str, FieldMetadata(alias="icdCode"), pydantic.Field(alias="icdCode")]
    is_chronic: typing_extensions.Annotated[str, FieldMetadata(alias="isChronic"), pydantic.Field(alias="isChronic")]
    id: str
    enterprise_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="enterpriseId"), pydantic.Field(alias="enterpriseId")
    ]
    practice_id: typing_extensions.Annotated[str, FieldMetadata(alias="practiceId"), pydantic.Field(alias="practiceId")]
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    health_concern: typing_extensions.Annotated[
        str, FieldMetadata(alias="healthConcern"), pydantic.Field(alias="healthConcern")
    ]
    category: str
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
