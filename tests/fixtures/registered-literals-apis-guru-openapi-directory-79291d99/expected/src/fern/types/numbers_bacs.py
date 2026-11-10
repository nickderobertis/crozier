

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NumbersBacs(UniversalBaseModel):
    """
    Identifying information for transferring money to or from a UK bank account via BACS.
    """

    account: str = pydantic.Field()
    """
    The BACS account number for the account
    """

    account_id: str = pydantic.Field()
    """
    The Plaid account ID associated with the account numbers
    """

    sort_code: str = pydantic.Field()
    """
    The BACS sort code for the account
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
