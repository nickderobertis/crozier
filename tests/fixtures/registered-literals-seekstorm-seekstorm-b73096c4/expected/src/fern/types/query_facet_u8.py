

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .query_facet_u8u8 import QueryFacetU8U8


class QueryFacetU8(UniversalBaseModel):
    """
    Range segment definition for numerical facet field values of type u8
    """

    u8: typing_extensions.Annotated[
        QueryFacetU8U8,
        FieldMetadata(alias="U8"),
        pydantic.Field(alias="U8", description="Range segment definition for numerical facet field values of type u8"),
    ]
    """
    Range segment definition for numerical facet field values of type u8
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
