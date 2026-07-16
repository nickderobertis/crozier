

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RiskEvaluation(UniversalBaseModel):
    """
    Represents fraud risk information for the associated payment.

    When you take a payment through Square's Payments API (using the `CreatePayment`
    endpoint), Square evaluates it and assigns a risk level to the payment. Sellers
    can use this information to determine the course of action (for example,
    provide the goods/services or refund the payment).
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when payment risk was evaluated, in RFC 3339 format.
    """

    risk_level: typing.Optional[str] = pydantic.Field(default=None)
    """
    The risk level associated with the payment
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
