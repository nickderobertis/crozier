

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Item5(UniversalBaseModel):
    enterprise_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="enterpriseId"), pydantic.Field(alias="enterpriseId")
    ]
    practice_id: typing_extensions.Annotated[str, FieldMetadata(alias="practiceId"), pydantic.Field(alias="practiceId")]
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    id: str
    completed_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="completedDate"), pydantic.Field(alias="completedDate")
    ]
    instrument: str
    score: str
    severity: str
    encounter_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterDate"), pydantic.Field(alias="encounterDate")
    ]
    create_timestamp: typing_extensions.Annotated[
        str, FieldMetadata(alias="createTimestamp"), pydantic.Field(alias="createTimestamp")
    ]
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
