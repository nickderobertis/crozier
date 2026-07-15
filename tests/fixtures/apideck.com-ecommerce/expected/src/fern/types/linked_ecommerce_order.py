

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ecommerce_order_status import EcommerceOrderStatus
from .id import Id


class LinkedEcommerceOrder(UniversalBaseModel):
    """
    The order this entity is linked to.
    """

    id: typing.Optional[Id] = None
    status: typing.Optional[EcommerceOrderStatus] = None
    total: typing.Optional[str] = pydantic.Field(default=None)
    """
    The total amount of the order.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
