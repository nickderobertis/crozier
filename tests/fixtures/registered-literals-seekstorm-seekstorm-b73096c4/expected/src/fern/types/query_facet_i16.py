

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .query_facet_i16i16 import QueryFacetI16I16


class QueryFacetI16(UniversalBaseModel):
    """
    Range segment definition for numerical facet field values of type i16
    """

    i16: typing_extensions.Annotated[
        QueryFacetI16I16,
        FieldMetadata(alias="I16"),
        pydantic.Field(
            alias="I16", description="Range segment definition for numerical facet field values of type i16"
        ),
    ]
    """
    Range segment definition for numerical facet field values of type i16
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
