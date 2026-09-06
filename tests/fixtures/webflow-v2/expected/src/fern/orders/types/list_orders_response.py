

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_orders_response_orders_item import ListOrdersResponseOrdersItem
from .list_orders_response_pagination import ListOrdersResponsePagination


class ListOrdersResponse(UniversalBaseModel):
    """
    Results from order list
    """

    orders: typing.Optional[typing.List[ListOrdersResponseOrdersItem]] = pydantic.Field(default=None)
    """
    List of orders
    """

    pagination: typing.Optional[ListOrdersResponsePagination] = pydantic.Field(default=None)
    """
    Pagination object
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
