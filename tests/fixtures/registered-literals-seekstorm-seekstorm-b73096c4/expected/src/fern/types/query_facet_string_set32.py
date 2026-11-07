

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .query_facet_string_set32string_set32 import QueryFacetStringSet32StringSet32


class QueryFacetStringSet32(UniversalBaseModel):
    """
    Facet field values of type string set
    """

    string_set32: typing_extensions.Annotated[
        QueryFacetStringSet32StringSet32,
        FieldMetadata(alias="StringSet32"),
        pydantic.Field(alias="StringSet32", description="Facet field values of type string set"),
    ]
    """
    Facet field values of type string set
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
