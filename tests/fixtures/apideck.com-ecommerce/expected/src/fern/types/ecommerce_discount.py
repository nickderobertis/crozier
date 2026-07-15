

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EcommerceDiscount(UniversalBaseModel):
    """
    An object representing a discount applied to an ecommerce order or product.
    """

    amount: typing.Optional[str] = pydantic.Field(default=None)
    """
    The fixed amount of the discount.
    """

    code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The code used to apply the discount.
    """

    percentage: typing.Optional[str] = pydantic.Field(default=None)
    """
    The percentage of the discount.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
