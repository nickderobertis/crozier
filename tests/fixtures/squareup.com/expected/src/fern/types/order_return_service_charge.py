

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .money import Money
from .order_line_item_applied_tax import OrderLineItemAppliedTax


class OrderReturnServiceCharge(UniversalBaseModel):
    """
    Represents the service charge applied to the original order.
    """

    amount_money: typing.Optional[Money] = None
    applied_money: typing.Optional[Money] = None
    applied_taxes: typing.Optional[typing.List[OrderLineItemAppliedTax]] = pydantic.Field(default=None)
    """
    The list of references to `OrderReturnTax` entities applied to the
    `OrderReturnServiceCharge`. Each `OrderLineItemAppliedTax` has a `tax_uid`
    that references the `uid` of a top-level `OrderReturnTax` that is being
    applied to the `OrderReturnServiceCharge`. On reads, the applied amount is
    populated.
    """

    calculation_phase: typing.Optional[str] = pydantic.Field(default=None)
    """
    The calculation phase after which to apply the service charge.
    """

    catalog_object_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The catalog object ID of the associated [OrderServiceCharge](https://developer.squareup.com/reference/square_2021-08-18/objects/OrderServiceCharge).
    """

    catalog_version: typing.Optional[int] = pydantic.Field(default=None)
    """
    The version of the catalog object that this service charge references.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the service charge.
    """

    percentage: typing.Optional[str] = pydantic.Field(default=None)
    """
    The percentage of the service charge, as a string representation of
    a decimal number. For example, a value of `"7.25"` corresponds to a
    percentage of 7.25%.
    
    Either `percentage` or `amount_money` should be set, but not both.
    """

    source_service_charge_uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The service charge `uid` from the order containing the original
    service charge. `source_service_charge_uid` is `null` for
    unlinked returns.
    """

    taxable: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether the surcharge can be taxed. Service charges
    calculated in the `TOTAL_PHASE` cannot be marked as taxable.
    """

    total_money: typing.Optional[Money] = None
    total_tax_money: typing.Optional[Money] = None
    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique ID that identifies the return service charge only within this order.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
