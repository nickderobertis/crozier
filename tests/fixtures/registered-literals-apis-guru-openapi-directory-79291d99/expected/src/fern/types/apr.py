

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .apr_apr_type import AprAprType


class Apr(UniversalBaseModel):
    """
    Information about the APR on the account.
    """

    apr_percentage: float = pydantic.Field()
    """
    Annual Percentage Rate applied.
    """

    apr_type: AprAprType = pydantic.Field()
    """
    The type of balance to which the APR applies.
    """

    balance_subject_to_apr: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount of money that is subjected to the APR if a balance was carried beyond payment due date. How it is calculated can vary by card issuer. It is often calculated as an average daily balance.
    """

    interest_charge_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount of money charged due to interest from last statement.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
