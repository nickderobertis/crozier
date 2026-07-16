

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bank_account import BankAccount
from .error import Error


class GetBankAccountResponse(UniversalBaseModel):
    """
    Response object returned by `GetBankAccount`.
    """

    bank_account: typing.Optional[BankAccount] = None
    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Information on errors encountered during the request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
