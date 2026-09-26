

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .links import Links


class PagingInfo(UniversalBaseModel):
    links: typing_extensions.Annotated[Links, FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]
    page_number: typing_extensions.Annotated[int, FieldMetadata(alias="pageNumber"), pydantic.Field(alias="pageNumber")]
    page_size: typing_extensions.Annotated[int, FieldMetadata(alias="pageSize"), pydantic.Field(alias="pageSize")]
    total_results: typing_extensions.Annotated[
        int, FieldMetadata(alias="totalResults"), pydantic.Field(alias="totalResults")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
