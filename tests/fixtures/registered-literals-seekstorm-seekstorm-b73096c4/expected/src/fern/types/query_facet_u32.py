

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .query_facet_u32u32 import QueryFacetU32U32


class QueryFacetU32(UniversalBaseModel):
    """
    Range segment definition for numerical facet field values of type u32
    """

    u32: typing_extensions.Annotated[
        QueryFacetU32U32,
        FieldMetadata(alias="U32"),
        pydantic.Field(
            alias="U32", description="Range segment definition for numerical facet field values of type u32"
        ),
    ]
    """
    Range segment definition for numerical facet field values of type u32
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
