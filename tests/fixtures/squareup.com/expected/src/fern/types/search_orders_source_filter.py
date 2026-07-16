

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SearchOrdersSourceFilter(UniversalBaseModel):
    """
    A filter based on order `source` information.
    """

    source_names: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Filters by the [Source](https://developer.squareup.com/reference/square_2021-08-18/objects/OrderSource) `name`. The filter returns any orders
    with a `source.name` that matches any of the listed source names.
    
    Max: 10 source names.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
