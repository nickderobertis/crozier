

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Ok83(UniversalBaseModel):
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    id: str
    description: str
    order: str
    category_id: typing_extensions.Annotated[str, FieldMetadata(alias="categoryId"), pydantic.Field(alias="categoryId")]
    category_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="categoryName"), pydantic.Field(alias="categoryName")
    ]
    cdc_race_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="cdcRaceCode"), pydantic.Field(alias="cdcRaceCode")
    ]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
