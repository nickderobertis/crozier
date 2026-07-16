

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OrderCreated(UniversalBaseModel):
    """ """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp for when the order was created, in RFC 3339 format.
    """

    location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the seller location that this order is associated with.
    """

    order_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The order's unique ID.
    """

    state: typing.Optional[str] = pydantic.Field(default=None)
    """
    The state of the order.
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
