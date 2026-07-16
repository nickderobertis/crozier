

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1money import V1Money


class V1PaymentDiscount(UniversalBaseModel):
    """
    V1PaymentDiscount
    """

    applied_money: typing.Optional[V1Money] = None
    discount_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the applied discount, if available. Discounts applied in older versions of Square Register might not have an ID.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The discount's name.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
