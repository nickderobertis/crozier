

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SearchOrdersSort(UniversalBaseModel):
    """
    Sorting criteria for a `SearchOrders` request. Results can only be sorted
    by a timestamp field.
    """

    sort_field: str = pydantic.Field()
    """
    The field to sort by.
    
    __Important:__ When using a [DateTimeFilter](https://developer.squareup.com/reference/square_2021-08-18/objects/SearchOrdersFilter),
    `sort_field` must match the timestamp field that the `DateTimeFilter` uses to
    filter. For example, if you set your `sort_field` to `CLOSED_AT` and you use a
    `DateTimeFilter`, your `DateTimeFilter` must filter for orders by their `CLOSED_AT` date.
    If this field does not match the timestamp field in `DateTimeFilter`,
    `SearchOrders` returns an error.
    
    Default: `CREATED_AT`.
    """

    sort_order: typing.Optional[str] = pydantic.Field(default=None)
    """
    The chronological order in which results are returned. Defaults to `DESC`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
