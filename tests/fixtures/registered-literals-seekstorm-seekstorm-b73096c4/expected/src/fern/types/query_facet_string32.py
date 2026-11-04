

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .query_facet_string32string32 import QueryFacetString32String32


class QueryFacetString32(UniversalBaseModel):
    """
    Facet field values of type string
    """

    string32: typing_extensions.Annotated[
        QueryFacetString32String32,
        FieldMetadata(alias="String32"),
        pydantic.Field(alias="String32", description="Facet field values of type string"),
    ]
    """
    Facet field values of type string
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
