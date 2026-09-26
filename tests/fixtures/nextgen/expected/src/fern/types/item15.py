

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Item15(UniversalBaseModel):
    id: str
    last_addressed_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="lastAddressedDate"), pydantic.Field(alias="lastAddressedDate")
    ]
    onset_date: typing_extensions.Annotated[str, FieldMetadata(alias="onsetDate"), pydantic.Field(alias="onsetDate")]
    description: str
    is_chronic: typing_extensions.Annotated[str, FieldMetadata(alias="isChronic"), pydantic.Field(alias="isChronic")]
    enterprise_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="enterpriseId"), pydantic.Field(alias="enterpriseId")
    ]
    practice_id: typing_extensions.Annotated[str, FieldMetadata(alias="practiceId"), pydantic.Field(alias="practiceId")]
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    health_concern: typing_extensions.Annotated[
        str, FieldMetadata(alias="healthConcern"), pydantic.Field(alias="healthConcern")
    ]
    category: str
    snomed_id: typing_extensions.Annotated[str, FieldMetadata(alias="snomedId"), pydantic.Field(alias="snomedId")]
    is_deleted: typing_extensions.Annotated[str, FieldMetadata(alias="isDeleted"), pydantic.Field(alias="isDeleted")]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
