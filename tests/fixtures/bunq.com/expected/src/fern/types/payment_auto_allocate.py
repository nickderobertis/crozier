

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .payment_auto_allocate_definition import PaymentAutoAllocateDefinition


class PaymentAutoAllocate(UniversalBaseModel):
    definition: typing.List[PaymentAutoAllocateDefinition] = pydantic.Field()
    """
    The definition of how the money should be allocated.
    """

    payment_id: int = pydantic.Field()
    """
    The payment that should be used to define the triggers for the payment auto allocate.
    """

    type: str = pydantic.Field()
    """
    Whether a payment should be sorted ONCE or RECURRING.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
