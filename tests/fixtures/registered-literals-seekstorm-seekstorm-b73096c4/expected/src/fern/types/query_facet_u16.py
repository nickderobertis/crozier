

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .query_facet_u16u16 import QueryFacetU16U16


class QueryFacetU16(UniversalBaseModel):
    """
    Range segment definition for numerical facet field values of type u16
    """

    u16: typing_extensions.Annotated[
        QueryFacetU16U16,
        FieldMetadata(alias="U16"),
        pydantic.Field(
            alias="U16", description="Range segment definition for numerical facet field values of type u16"
        ),
    ]
    """
    Range segment definition for numerical facet field values of type u16
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
