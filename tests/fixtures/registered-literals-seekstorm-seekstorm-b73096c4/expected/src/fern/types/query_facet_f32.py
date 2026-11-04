

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .query_facet_f32f32 import QueryFacetF32F32


class QueryFacetF32(UniversalBaseModel):
    """
    Range segment definition for numerical facet field values of type f32
    """

    f32: typing_extensions.Annotated[
        QueryFacetF32F32,
        FieldMetadata(alias="F32"),
        pydantic.Field(
            alias="F32", description="Range segment definition for numerical facet field values of type f32"
        ),
    ]
    """
    Range segment definition for numerical facet field values of type f32
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
