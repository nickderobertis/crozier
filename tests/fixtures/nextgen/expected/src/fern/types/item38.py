

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Item38(UniversalBaseModel):
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    enterprise_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="enterpriseId"), pydantic.Field(alias="enterpriseId")
    ]
    practice_id: typing_extensions.Annotated[str, FieldMetadata(alias="practiceId"), pydantic.Field(alias="practiceId")]
    encounter_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="encounterDate"), pydantic.Field(alias="encounterDate")
    ]
    tobacco_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="tobaccoType"), pydantic.Field(alias="tobaccoType")
    ]
    tobacco_status: typing_extensions.Annotated[
        str, FieldMetadata(alias="tobaccoStatus"), pydantic.Field(alias="tobaccoStatus")
    ]
    smoking_status: typing_extensions.Annotated[
        str, FieldMetadata(alias="smokingStatus"), pydantic.Field(alias="smokingStatus")
    ]
    usage_per_day: typing_extensions.Annotated[
        str, FieldMetadata(alias="usagePerDay"), pydantic.Field(alias="usagePerDay")
    ]
    pack_years: typing_extensions.Annotated[str, FieldMetadata(alias="packYears"), pydantic.Field(alias="packYears")]
    date_quit: typing_extensions.Annotated[str, FieldMetadata(alias="dateQuit"), pydantic.Field(alias="dateQuit")]
    tobacco_health_concern: typing_extensions.Annotated[
        str, FieldMetadata(alias="tobaccoHealthConcern"), pydantic.Field(alias="tobaccoHealthConcern")
    ]
    tobacco_category: typing_extensions.Annotated[
        str, FieldMetadata(alias="tobaccoCategory"), pydantic.Field(alias="tobaccoCategory")
    ]
    smoking_health_concern: typing_extensions.Annotated[
        str, FieldMetadata(alias="smokingHealthConcern"), pydantic.Field(alias="smokingHealthConcern")
    ]
    smoking_category: typing_extensions.Annotated[
        str, FieldMetadata(alias="smokingCategory"), pydantic.Field(alias="smokingCategory")
    ]
    id: str
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
