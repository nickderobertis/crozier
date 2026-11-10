

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ach_class import AchClass
from .transfer_amount import TransferAmount
from .transfer_funding_account_id_response import TransferFundingAccountIdResponse
from .transfer_type import TransferType
from .transfer_user_in_response import TransferUserInResponse


class TransferAuthorizationProposedTransfer(UniversalBaseModel):
    """
    Details regarding the proposed transfer.
    """

    account_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Plaid `account_id` for the account that will be debited or credited.
    """

    ach_class: typing.Optional[AchClass] = None
    amount: TransferAmount
    funding_account_id: TransferFundingAccountIdResponse
    iso_currency_code: str = pydantic.Field()
    """
    The currency of the transfer amount. The default value is "USD".
    """

    network: str = pydantic.Field()
    """
    The network or rails used for the transfer.
    """

    origination_account_id: str = pydantic.Field()
    """
    Plaid's unique identifier for the origination account that was used for this transfer.
    """

    originator_client_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Plaid client ID that is the originator of this transfer. Only present if created on behalf of another client as a third-party sender (TPS).
    """

    type: TransferType
    user: TransferUserInResponse

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
