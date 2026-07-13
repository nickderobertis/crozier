

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TransferwiseAccountQuoteRead(UniversalBaseModel):
    account_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Transferwise's id of the account.
    """

    account_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The account number.
    """

    bank_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The bank code.
    """

    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    The country of the account.
    """

    currency: typing.Optional[str] = pydantic.Field(default=None)
    """
    The currency the account.
    """

    name_account_holder: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the account holder.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
