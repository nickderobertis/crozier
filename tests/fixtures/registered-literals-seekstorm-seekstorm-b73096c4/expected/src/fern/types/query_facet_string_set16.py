

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .query_facet_string_set16string_set16 import QueryFacetStringSet16StringSet16


class QueryFacetStringSet16(UniversalBaseModel):
    """
    Facet field values of type string set
    """

    string_set16: typing_extensions.Annotated[
        QueryFacetStringSet16StringSet16,
        FieldMetadata(alias="StringSet16"),
        pydantic.Field(alias="StringSet16", description="Facet field values of type string set"),
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
