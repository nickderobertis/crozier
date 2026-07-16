

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OrderEntry(UniversalBaseModel):
    """
    A lightweight description of an [order](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) that is returned when
    `returned_entries` is `true` on a [SearchOrdersRequest](https://developer.squareup.com/reference/square_2021-08-18/orders-api/search-orders).
    """

    location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The location ID the order belongs to.
    """

    order_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the order.
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    The version number, which is incremented each time an update is committed to the order.
    Orders that were not created through the API do not include a version number and
    therefore cannot be updated.
    
    [Read more about working with versions.](https://developer.squareup.com/docs/orders-api/manage-orders#update-orders)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
