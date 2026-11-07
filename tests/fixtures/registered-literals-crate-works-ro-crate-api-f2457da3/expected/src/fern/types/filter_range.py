

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .filter_range_gte import FilterRangeGte
from .filter_range_lte import FilterRangeLte


class FilterRange(UniversalBaseModel):
    """
    An inclusive range constraint for a search filter. Valid only for filters declared with type `date` or `number` in `/capabilities`. At least one bound is required; values are ISO 8601 strings for `date` filters and numbers for `number` filters. A filter value may be a single range or a non-empty array of ranges; an array is matched as an OR of its ranges — an entity matches when any of the ranges matches.
    """

    gte: typing.Optional[FilterRangeGte] = pydantic.Field(default=None)
    """
    The inclusive lower bound.
    """

    lte: typing.Optional[FilterRangeLte] = pydantic.Field(default=None)
    """
    The inclusive upper bound.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
