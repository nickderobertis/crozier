

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .money import Money


class OrderLineItemAppliedTax(UniversalBaseModel):
    """
    Represents an applied portion of a tax to a line item in an order.

    Order-scoped taxes automatically include the applied taxes in each line item.
    Line item taxes must be referenced from any applicable line items.
    The corresponding applied money is automatically computed, based on the
    set of participating line items.
    """

    applied_money: typing.Optional[Money] = None
    tax_uid: str = pydantic.Field()
    """
    The `uid` of the tax for which this applied tax represents. It must reference
    a tax present in the `order.taxes` field.
    
    This field is immutable. To change which taxes apply to a line item, delete and add a new
    `OrderLineItemAppliedTax`.
    """

    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique ID that identifies the applied tax only within this order.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
