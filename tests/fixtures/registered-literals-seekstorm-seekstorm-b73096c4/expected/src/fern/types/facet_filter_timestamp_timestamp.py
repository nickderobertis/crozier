

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .range_i64 import RangeI64


class FacetFilterTimestampTimestamp(UniversalBaseModel):
    """
    Timestamp range filter, Unix timestamp: the number of seconds since 1 January 1970
    """

    field: str = pydantic.Field()
    """
    field name
    """

    filter: RangeI64 = pydantic.Field()
    """
    filter: range start, range end
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
