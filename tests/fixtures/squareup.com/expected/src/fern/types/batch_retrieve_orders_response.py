

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error import Error
from .order import Order


class BatchRetrieveOrdersResponse(UniversalBaseModel):
    """
    Defines the fields that are included in the response body of
    a request to the `BatchRetrieveOrders` endpoint.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    orders: typing.Optional[typing.List[Order]] = pydantic.Field(default=None)
    """
    The requested orders. This will omit any requested orders that do not exist.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
