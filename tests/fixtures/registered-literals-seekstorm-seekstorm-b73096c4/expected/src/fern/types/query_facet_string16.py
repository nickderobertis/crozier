

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .query_facet_string16string16 import QueryFacetString16String16


class QueryFacetString16(UniversalBaseModel):
    """
    Facet field values of type string
    """

    string16: typing_extensions.Annotated[
        QueryFacetString16String16,
        FieldMetadata(alias="String16"),
        pydantic.Field(alias="String16", description="Facet field values of type string"),
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
