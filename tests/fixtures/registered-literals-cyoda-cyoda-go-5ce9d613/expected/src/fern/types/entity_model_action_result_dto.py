

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .entity_model_key import EntityModelKey


class EntityModelActionResultDto(UniversalBaseModel):
    success: bool
    model_key: typing_extensions.Annotated[
        EntityModelKey, FieldMetadata(alias="modelKey"), pydantic.Field(alias="modelKey")
    ]
    message: str
    model_id: typing_extensions.Annotated[str, FieldMetadata(alias="modelId"), pydantic.Field(alias="modelId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
