

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amount import Amount
from .error import Error
from .label_monetary_account import LabelMonetaryAccount


class SofortMerchantTransactionRead(UniversalBaseModel):
    alias: typing.Optional[LabelMonetaryAccount] = pydantic.Field(default=None)
    """
    The alias of the monetary account to add money to.
    """

    amount_guaranteed: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    In case of a successful transaction, the amount of money that will be transferred.
    """

    amount_requested: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The requested amount of money to add.
    """

    counterparty_alias: typing.Optional[LabelMonetaryAccount] = pydantic.Field(default=None)
    """
    The alias of the monetary account the money comes from.
    """

    error_message: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    The error message of the transaction.
    """

    issuer: typing.Optional[str] = pydantic.Field(default=None)
    """
    The BIC of the issuer.
    """

    issuer_authentication_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL to visit to 
    """

    monetary_account_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the monetary account this sofort merchant transaction links to.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the transaction.
    """

    transaction_identifier: typing.Optional[str] = pydantic.Field(default=None)
    """
    The 'transaction ID' of the Sofort transaction.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
