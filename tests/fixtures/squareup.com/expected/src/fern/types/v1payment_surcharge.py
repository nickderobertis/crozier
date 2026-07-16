

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1money import V1Money
from .v1payment_tax import V1PaymentTax


class V1PaymentSurcharge(UniversalBaseModel):
    """
    V1PaymentSurcharge
    """

    amount_money: typing.Optional[V1Money] = None
    applied_money: typing.Optional[V1Money] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the surcharge.
    """

    rate: typing.Optional[str] = pydantic.Field(default=None)
    """
    The amount of the surcharge as a percentage. The percentage is provided as a string representing the decimal equivalent of the percentage. For example, "0.7" corresponds to a 7% surcharge. Exactly one of rate or amount_money should be set.
    """

    surcharge_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A Square-issued unique identifier associated with the surcharge.
    """

    taxable: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether the surcharge is taxable.
    """

    taxes: typing.Optional[typing.List[V1PaymentTax]] = pydantic.Field(default=None)
    """
    The list of taxes that should be applied to the surcharge.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates the source of the surcharge. For example, if it was applied as an automatic gratuity for a large group.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
