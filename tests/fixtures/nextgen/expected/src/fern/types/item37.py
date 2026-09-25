

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Item37(UniversalBaseModel):
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    enterprise_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="enterpriseId"), pydantic.Field(alias="enterpriseId")
    ]
    practice_id: typing_extensions.Annotated[str, FieldMetadata(alias="practiceId"), pydantic.Field(alias="practiceId")]
    id: str
    encounter_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterId"), pydantic.Field(alias="encounterId")
    ]
    encounter_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterTimestamp"), pydantic.Field(alias="encounterTimestamp")
    ]
    service_item_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="serviceItemId"), pydantic.Field(alias="serviceItemId")
    ]
    service_item_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="serviceItemDescription"), pydantic.Field(alias="serviceItemDescription")
    ]
    cpt4code: typing_extensions.Annotated[str, FieldMetadata(alias="cpt4Code"), pydantic.Field(alias="cpt4Code")]
    service_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="serviceDate"), pydantic.Field(alias="serviceDate")
    ]
    is_deleted: typing_extensions.Annotated[str, FieldMetadata(alias="isDeleted"), pydantic.Field(alias="isDeleted")]
    is_completed: typing_extensions.Annotated[
        str, FieldMetadata(alias="isCompleted"), pydantic.Field(alias="isCompleted")
    ]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
