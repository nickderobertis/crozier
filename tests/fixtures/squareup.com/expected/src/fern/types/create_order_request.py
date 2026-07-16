

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .order import Order


class CreateOrderRequest(UniversalBaseModel):
    """ """

    idempotency_key: typing.Optional[str] = pydantic.Field(default=None)
    """
    A value you specify that uniquely identifies this
    order among orders you have created.
    
    If you are unsure whether a particular order was created successfully,
    you can try it again with the same idempotency key without
    worrying about creating duplicate orders.
    
    For more information, see [Idempotency](https://developer.squareup.com/docs/basics/api101/idempotency).
    """

    order: typing.Optional[Order] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
