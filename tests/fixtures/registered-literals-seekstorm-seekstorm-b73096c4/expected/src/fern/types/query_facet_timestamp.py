

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .query_facet_timestamp_timestamp import QueryFacetTimestampTimestamp


class QueryFacetTimestamp(UniversalBaseModel):
    """
    Range segment definition for numerical facet field values of type Unix timestamp
    """

    timestamp: typing_extensions.Annotated[
        QueryFacetTimestampTimestamp,
        FieldMetadata(alias="Timestamp"),
        pydantic.Field(
            alias="Timestamp",
            description="Range segment definition for numerical facet field values of type Unix timestamp",
        ),
    ]
    """
    Range segment definition for numerical facet field values of type Unix timestamp
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
