

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .payment_allocations_item_type import PaymentAllocationsItemType


class PaymentAllocationsItem(UniversalBaseModel):
    amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount of payment that should be attributed to this allocation. If null, the total_amount will be used.
    """

    code: typing.Optional[str] = None
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier of entity this payment should be attributed to.
    """

    type: typing.Optional[PaymentAllocationsItemType] = pydantic.Field(default=None)
    """
    Type of entity this payment should be attributed to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
