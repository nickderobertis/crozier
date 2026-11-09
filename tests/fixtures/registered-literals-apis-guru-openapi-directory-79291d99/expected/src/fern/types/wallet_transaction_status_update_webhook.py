

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .wallet_transaction_status import WalletTransactionStatus
from .webhook_environment_values import WebhookEnvironmentValues


class WalletTransactionStatusUpdateWebhook(UniversalBaseModel):
    """
    Fired when the status of a wallet transaction has changed.
    """

    environment: WebhookEnvironmentValues
    new_status: WalletTransactionStatus
    old_status: WalletTransactionStatus
    payment_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The `payment_id` associated with the transaction. This will be present in case of `REFUND` and `PIS_PAY_IN`
    """

    timestamp: dt.datetime = pydantic.Field()
    """
    The timestamp of the update, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format, e.g. `"2017-09-14T14:42:19.350Z"`
    """

    transaction_id: str = pydantic.Field()
    """
    The `transaction_id` for the wallet transaction being updated
    """

    wallet_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The EMI (E-Money Institution) wallet that this payment is associated with. This wallet is used as an intermediary account to enable Plaid to reconcile the settlement of funds for Payment Initiation requests.
    """

    webhook_code: str = pydantic.Field()
    """
    `WALLET_TRANSACTION_STATUS_UPDATE`
    """

    webhook_type: str = pydantic.Field()
    """
    `WALLET`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
