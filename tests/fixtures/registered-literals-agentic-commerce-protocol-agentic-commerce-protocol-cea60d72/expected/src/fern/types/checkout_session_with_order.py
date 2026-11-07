

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .checkout_session_base import CheckoutSessionBase
from .order import Order


class CheckoutSessionWithOrder(CheckoutSessionBase):
    order: Order

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
