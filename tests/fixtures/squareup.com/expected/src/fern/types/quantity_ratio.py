

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class QuantityRatio(UniversalBaseModel):
    """
    A whole number or unreduced fractional ratio.
    """

    quantity: typing.Optional[int] = pydantic.Field(default=None)
    """
    The whole or fractional quantity as the numerator.
    """

    quantity_denominator: typing.Optional[int] = pydantic.Field(default=None)
    """
    The whole or fractional quantity as the denominator. 
    In the case of fractional quantity this field is the denominator and quantity is the numerator.
    When unspecified, the value is `1`. For example, when `quantity=3` and `quantity_donominator` is unspecified,
    the quantity ratio is `3` or `3/1`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
