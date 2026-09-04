

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Balance(UniversalBaseModel):
    currency: str = pydantic.Field()
    """
    The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes).
    """

    fee: int = pydantic.Field()
    """
    The amount of the grant fee.
    """

    principal: int = pydantic.Field()
    """
    The grant amount that is paid out to the user for business financing.
    """

    total: int = pydantic.Field()
    """
    The total amount of the grant that the user must repay. It is the sum of the fee amount and the principal amount.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
