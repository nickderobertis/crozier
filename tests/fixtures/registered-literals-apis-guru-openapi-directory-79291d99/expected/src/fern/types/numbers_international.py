

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NumbersInternational(UniversalBaseModel):
    """
    Identifying information for transferring money to or from an international bank account via wire transfer.
    """

    account_id: str = pydantic.Field()
    """
    The Plaid account ID associated with the account numbers
    """

    bic: str = pydantic.Field()
    """
    The Bank Identifier Code (BIC) for the account
    """

    iban: str = pydantic.Field()
    """
    The International Bank Account Number (IBAN) for the account
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
