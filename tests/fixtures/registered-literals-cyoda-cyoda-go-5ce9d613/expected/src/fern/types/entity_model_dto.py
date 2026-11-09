

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class EntityModelDto(UniversalBaseModel):
    id: str
    model_name: typing_extensions.Annotated[str, FieldMetadata(alias="modelName"), pydantic.Field(alias="modelName")]
    model_version: typing_extensions.Annotated[
        int, FieldMetadata(alias="modelVersion"), pydantic.Field(alias="modelVersion")
    ]
    current_state: typing_extensions.Annotated[
        str, FieldMetadata(alias="currentState"), pydantic.Field(alias="currentState")
    ]
    model_update_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="modelUpdateDate"), pydantic.Field(alias="modelUpdateDate")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
