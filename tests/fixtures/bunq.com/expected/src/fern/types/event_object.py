

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .bank_switch_service_netherlands_incoming_payment import BankSwitchServiceNetherlandsIncomingPayment
from .bunq_me_fundraiser_result import BunqMeFundraiserResult
from .bunq_me_tab import BunqMeTab
from .bunq_me_tab_result_response import BunqMeTabResultResponse
from .card import Card
from .card_debit import CardDebit
from .draft_payment import DraftPayment
from .feature_announcement import FeatureAnnouncement
from .ideal_merchant_transaction import IdealMerchantTransaction
from .invoice import Invoice
from .master_card_action import MasterCardAction
from .request_inquiry import RequestInquiry
from .request_inquiry_batch import RequestInquiryBatch
from .request_response import RequestResponse
from .reward_recipient import RewardRecipient
from .reward_sender import RewardSender
from .schedule_instance import ScheduleInstance
from .schedule_payment import SchedulePayment
from .schedule_payment_batch import SchedulePaymentBatch
from .share_invite_monetary_account_inquiry import ShareInviteMonetaryAccountInquiry
from .share_invite_monetary_account_response import ShareInviteMonetaryAccountResponse
from .sofort_merchant_transaction import SofortMerchantTransaction
from .transferwise_transfer import TransferwiseTransfer


class EventObject(UniversalBaseModel):
    bank_switch_service_netherlands_incoming_payment: typing_extensions.Annotated[
        typing.Optional[BankSwitchServiceNetherlandsIncomingPayment],
        FieldMetadata(alias="BankSwitchServiceNetherlandsIncomingPayment"),
        pydantic.Field(alias="BankSwitchServiceNetherlandsIncomingPayment", description=""),
    ] = None
    """
    
    """

    bunq_me_fundraiser_result: typing_extensions.Annotated[
        typing.Optional[BunqMeFundraiserResult],
        FieldMetadata(alias="BunqMeFundraiserResult"),
        pydantic.Field(alias="BunqMeFundraiserResult", description=""),
    ] = None
    """
    
    """

    bunq_me_tab: typing_extensions.Annotated[
        typing.Optional[BunqMeTab], FieldMetadata(alias="BunqMeTab"), pydantic.Field(alias="BunqMeTab", description="")
    ] = None
    """
    
    """

    bunq_me_tab_result_response: typing_extensions.Annotated[
        typing.Optional[BunqMeTabResultResponse],
        FieldMetadata(alias="BunqMeTabResultResponse"),
        pydantic.Field(alias="BunqMeTabResultResponse", description=""),
    ] = None
    """
    
    """

    card: typing_extensions.Annotated[
        typing.Optional[Card], FieldMetadata(alias="Card"), pydantic.Field(alias="Card", description="")
    ] = None
    """
    
    """

    card_debit: typing_extensions.Annotated[
        typing.Optional[CardDebit], FieldMetadata(alias="CardDebit"), pydantic.Field(alias="CardDebit", description="")
    ] = None
    """
    
    """

    draft_payment: typing_extensions.Annotated[
        typing.Optional[DraftPayment],
        FieldMetadata(alias="DraftPayment"),
        pydantic.Field(alias="DraftPayment", description=""),
    ] = None
    """
    
    """

    feature_announcement: typing_extensions.Annotated[
        typing.Optional[FeatureAnnouncement],
        FieldMetadata(alias="FeatureAnnouncement"),
        pydantic.Field(alias="FeatureAnnouncement", description=""),
    ] = None
    """
    
    """

    ideal_merchant_transaction: typing_extensions.Annotated[
        typing.Optional[IdealMerchantTransaction],
        FieldMetadata(alias="IdealMerchantTransaction"),
        pydantic.Field(alias="IdealMerchantTransaction", description=""),
    ] = None
    """
    
    """

    invoice: typing_extensions.Annotated[
        typing.Optional[Invoice], FieldMetadata(alias="Invoice"), pydantic.Field(alias="Invoice", description="")
    ] = None
    """
    
    """

    master_card_action: typing_extensions.Annotated[
        typing.Optional[MasterCardAction],
        FieldMetadata(alias="MasterCardAction"),
        pydantic.Field(alias="MasterCardAction", description=""),
    ] = None
    """
    
    """

    payment: typing_extensions.Annotated[
        typing.Optional["Payment"], FieldMetadata(alias="Payment"), pydantic.Field(alias="Payment", description="")
    ] = None
    """
    
    """

    payment_batch: typing_extensions.Annotated[
        typing.Optional["PaymentBatch"],
        FieldMetadata(alias="PaymentBatch"),
        pydantic.Field(alias="PaymentBatch", description=""),
    ] = None
    """
    
    """

    request_inquiry: typing_extensions.Annotated[
        typing.Optional[RequestInquiry],
        FieldMetadata(alias="RequestInquiry"),
        pydantic.Field(alias="RequestInquiry", description=""),
    ] = None
    """
    
    """

    request_inquiry_batch: typing_extensions.Annotated[
        typing.Optional[RequestInquiryBatch],
        FieldMetadata(alias="RequestInquiryBatch"),
        pydantic.Field(alias="RequestInquiryBatch", description=""),
    ] = None
    """
    
    """

    request_response: typing_extensions.Annotated[
        typing.Optional[RequestResponse],
        FieldMetadata(alias="RequestResponse"),
        pydantic.Field(alias="RequestResponse", description=""),
    ] = None
    """
    
    """

    reward_recipient: typing_extensions.Annotated[
        typing.Optional[RewardRecipient],
        FieldMetadata(alias="RewardRecipient"),
        pydantic.Field(alias="RewardRecipient", description=""),
    ] = None
    """
    
    """

    reward_sender: typing_extensions.Annotated[
        typing.Optional[RewardSender],
        FieldMetadata(alias="RewardSender"),
        pydantic.Field(alias="RewardSender", description=""),
    ] = None
    """
    
    """

    scheduled_instance: typing_extensions.Annotated[
        typing.Optional[ScheduleInstance],
        FieldMetadata(alias="ScheduledInstance"),
        pydantic.Field(alias="ScheduledInstance", description=""),
    ] = None
    """
    
    """

    scheduled_payment: typing_extensions.Annotated[
        typing.Optional[SchedulePayment],
        FieldMetadata(alias="ScheduledPayment"),
        pydantic.Field(alias="ScheduledPayment", description=""),
    ] = None
    """
    
    """

    scheduled_payment_batch: typing_extensions.Annotated[
        typing.Optional[SchedulePaymentBatch],
        FieldMetadata(alias="ScheduledPaymentBatch"),
        pydantic.Field(alias="ScheduledPaymentBatch", description=""),
    ] = None
    """
    
    """

    share_invite_bank_inquiry: typing_extensions.Annotated[
        typing.Optional[ShareInviteMonetaryAccountInquiry],
        FieldMetadata(alias="ShareInviteBankInquiry"),
        pydantic.Field(alias="ShareInviteBankInquiry", description=""),
    ] = None
    """
    
    """

    share_invite_bank_response: typing_extensions.Annotated[
        typing.Optional[ShareInviteMonetaryAccountResponse],
        FieldMetadata(alias="ShareInviteBankResponse"),
        pydantic.Field(alias="ShareInviteBankResponse", description=""),
    ] = None
    """
    
    """

    sofort_merchant_transaction: typing_extensions.Annotated[
        typing.Optional[SofortMerchantTransaction],
        FieldMetadata(alias="SofortMerchantTransaction"),
        pydantic.Field(alias="SofortMerchantTransaction", description=""),
    ] = None
    """
    
    """

    transferwise_payment: typing_extensions.Annotated[
        typing.Optional[TransferwiseTransfer],
        FieldMetadata(alias="TransferwisePayment"),
        pydantic.Field(alias="TransferwisePayment", description=""),
    ] = None
    """
    
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .payment import Payment
from .payment_auto_allocate_instance import PaymentAutoAllocateInstance
from .payment_batch import PaymentBatch
from .payment_batch_anchored_payment import PaymentBatchAnchoredPayment

update_forward_refs(
    EventObject,
    Payment=Payment,
    PaymentAutoAllocateInstance=PaymentAutoAllocateInstance,
    PaymentBatch=PaymentBatch,
    PaymentBatchAnchoredPayment=PaymentBatchAnchoredPayment,
)
