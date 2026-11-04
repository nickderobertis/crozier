

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .query_facet_i8i8 import QueryFacetI8I8


class QueryFacetI8(UniversalBaseModel):
    """
    Range segment definition for numerical facet field values of type i8
    """

    i8: typing_extensions.Annotated[
        QueryFacetI8I8,
        FieldMetadata(alias="I8"),
        pydantic.Field(alias="I8", description="Range segment definition for numerical facet field values of type i8"),
    ]
    """
    Range segment definition for numerical facet field values of type i8
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
