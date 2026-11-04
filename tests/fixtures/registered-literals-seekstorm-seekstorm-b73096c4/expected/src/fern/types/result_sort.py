

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .facet_value import FacetValue
from .sort_order import SortOrder


class ResultSort(UniversalBaseModel):
    """
    Specifies the sort order for the search results.
    """

    field: str = pydantic.Field()
    """
    name of the facet field to sort by
    """

    order: SortOrder = pydantic.Field()
    """
    Sort order: Ascending or Descending
    """

    base: FacetValue = pydantic.Field()
    """
    Base value/point for (geo) proximity sorting
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
