

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .range_type import RangeType


class QueryFacetI64I64(UniversalBaseModel):
    """
    Range segment definition for numerical facet field values of type i64
    """

    field: str = pydantic.Field()
    """
    field name
    """

    range_type: RangeType = pydantic.Field()
    """
    range type (CountWithinRange,CountBelowRange,CountAboveRange)
    """

    ranges: typing.List[typing.List[typing.Any]] = pydantic.Field()
    """
    range label, range start
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
