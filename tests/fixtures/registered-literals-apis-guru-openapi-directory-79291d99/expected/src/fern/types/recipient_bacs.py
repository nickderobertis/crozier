

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RecipientBacs(UniversalBaseModel):
    """
    An object containing a BACS account number and sort code. If an IBAN is not provided or if you need to accept domestic GBP-denominated payments, BACS data is required.
    """

    account: typing.Optional[str] = pydantic.Field(default=None)
    """
    The account number of the account. Maximum of 10 characters.
    """

    sort_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The 6-character sort code of the account.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
