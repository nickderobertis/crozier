

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NumbersEft(UniversalBaseModel):
    """
    Identifying information for transferring money to or from a Canadian bank account via EFT.
    """

    account: str = pydantic.Field()
    """
    The EFT account number for the account
    """

    account_id: str = pydantic.Field()
    """
    The Plaid account ID associated with the account numbers
    """

    branch: str = pydantic.Field()
    """
    The EFT branch number for the account
    """

    institution: str = pydantic.Field()
    """
    The EFT institution number for the account
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
