

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .facet_filter_timestamp_timestamp import FacetFilterTimestampTimestamp


class FacetFilterTimestamp(UniversalBaseModel):
    """
    Timestamp range filter, Unix timestamp: the number of seconds since 1 January 1970
    """

    timestamp: typing_extensions.Annotated[
        FacetFilterTimestampTimestamp,
        FieldMetadata(alias="Timestamp"),
        pydantic.Field(
            alias="Timestamp",
            description="Timestamp range filter, Unix timestamp: the number of seconds since 1 January 1970",
        ),
    ]
    """
    Timestamp range filter, Unix timestamp: the number of seconds since 1 January 1970
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
