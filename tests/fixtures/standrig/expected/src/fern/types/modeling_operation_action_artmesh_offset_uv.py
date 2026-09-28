

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ModelingOperationActionArtmeshOffsetUv(UniversalBaseModel):
    min_u: typing_extensions.Annotated[float, FieldMetadata(alias="minU"), pydantic.Field(alias="minU")]
    max_u: typing_extensions.Annotated[float, FieldMetadata(alias="maxU"), pydantic.Field(alias="maxU")]
    min_v: typing_extensions.Annotated[float, FieldMetadata(alias="minV"), pydantic.Field(alias="minV")]
    max_v: typing_extensions.Annotated[float, FieldMetadata(alias="maxV"), pydantic.Field(alias="maxV")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
