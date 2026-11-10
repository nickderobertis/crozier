

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ach_class import AchClass
from .transfer_amount import TransferAmount
from .transfer_authorization_guarantee_decision import TransferAuthorizationGuaranteeDecision
from .transfer_authorization_guarantee_decision_rationale import TransferAuthorizationGuaranteeDecisionRationale
from .transfer_expected_settlement_schedule_item import TransferExpectedSettlementScheduleItem
from .transfer_failure import TransferFailure
from .transfer_funding_account_id_response import TransferFundingAccountIdResponse
from .transfer_id import TransferId
from .transfer_metadata import TransferMetadata
from .transfer_network import TransferNetwork
from .transfer_refund import TransferRefund
from .transfer_status import TransferStatus
from .transfer_sweep_status import TransferSweepStatus
from .transfer_type import TransferType
from .transfer_user_in_response import TransferUserInResponse


class Transfer(UniversalBaseModel):
    """
    Represents a transfer within the Transfers API.
    """

    account_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Plaid `account_id` corresponding to the end-user account that will be debited or credited.
    """

    ach_class: typing.Optional[AchClass] = None
    amount: TransferAmount
    cancellable: bool = pydantic.Field()
    """
    When `true`, you can still cancel this transfer.
    """

    created: dt.datetime = pydantic.Field()
    """
    The datetime when this transfer was created. This will be of the form `2006-01-02T15:04:05Z`
    """

    description: str = pydantic.Field()
    """
    The description of the transfer.
    """

    expected_settlement_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The expected date when the full amount of the transfer settles at the consumers’ account, if the transfer is credit; or at the customer's business checking account, if the transfer is debit. Only set for ACH transfers and is null for non-ACH transfers. Only set for ACH transfers. This will be of the form YYYY-MM-DD.
    """

    expected_settlement_schedule: typing.Optional[typing.List[TransferExpectedSettlementScheduleItem]] = pydantic.Field(
        default=None
    )
    """
    The expected settlement schedule of this transfer, if posted. Only applies to ACH debit transfers.
    """

    failure_reason: typing.Optional[TransferFailure] = None
    funding_account_id: TransferFundingAccountIdResponse
    guarantee_decision: typing.Optional[TransferAuthorizationGuaranteeDecision] = None
    guarantee_decision_rationale: typing.Optional[TransferAuthorizationGuaranteeDecisionRationale] = None
    id: TransferId
    iso_currency_code: str = pydantic.Field()
    """
    The currency of the transfer amount, e.g. "USD"
    """

    metadata: typing.Optional[TransferMetadata] = None
    network: TransferNetwork
    origination_account_id: str = pydantic.Field()
    """
    Plaid’s unique identifier for the origination account that was used for this transfer.
    """

    originator_client_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Plaid client ID that is the originator of this transfer. Only present if created on behalf of another client as a third-party sender (TPS).
    """

    recurring_transfer_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the recurring transfer if this transfer belongs to a recurring transfer.
    """

    refunds: typing.List[TransferRefund] = pydantic.Field()
    """
    A list of refunds associated with this transfer.
    """

    settled_amount: typing.Optional[str] = pydantic.Field(default=None)
    """
    The accumulated amount that have been swept to date. This number does not reflect `return_swept` amount if the transfer is returned. Only applies to ACH debit transfers.
    """

    standard_return_window: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The date 3 business days from settlement date indicating the following ACH returns can no longer happen: R01, R02, R03, R29. This will be of the form YYYY-MM-DD.
    """

    status: TransferStatus
    sweep_status: typing.Optional[TransferSweepStatus] = None
    type: TransferType
    unauthorized_return_window: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The date 61 business days from settlement date indicating the following ACH returns can no longer happen: R05, R07, R10, R11, R51, R33, R37, R38, R51, R52, R53. This will be of the form YYYY-MM-DD.
    """

    user: TransferUserInResponse

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
