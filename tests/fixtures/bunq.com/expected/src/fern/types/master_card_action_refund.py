

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .additional_information import AdditionalInformation
from .amount import Amount
from .attachment_master_card_action_refund import AttachmentMasterCardActionRefund
from .label_card import LabelCard
from .label_monetary_account import LabelMonetaryAccount
from .label_user import LabelUser
from .master_card_action_reference import MasterCardActionReference


class MasterCardActionRefund(UniversalBaseModel):
    additional_information: typing.Optional[AdditionalInformation] = pydantic.Field(default=None)
    """
    All additional information provided by the user.
    """

    alias: typing.Optional[LabelMonetaryAccount] = pydantic.Field(default=None)
    """
    The monetary account label of the account that this action is created for.
    """

    amount: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The amount to refund.
    """

    attachment: typing.Optional[typing.List[AttachmentMasterCardActionRefund]] = pydantic.Field(default=None)
    """
    The Attachments to attach to the refund request.
    """

    category: typing.Optional[str] = pydantic.Field(default=None)
    """
    The category of the refund, required for chargeback.
    """

    comment: typing.Optional[str] = pydantic.Field(default=None)
    """
    Comment about the refund.
    """

    counterparty_alias: typing.Optional[LabelMonetaryAccount] = pydantic.Field(default=None)
    """
    The monetary account label of the counterparty.
    """

    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the refund's creation.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description for this transaction to display.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the refund.
    """

    label_card: typing.Optional[LabelCard] = pydantic.Field(default=None)
    """
    The label of the card.
    """

    label_user_creator: typing.Optional[LabelUser] = pydantic.Field(default=None)
    """
    The label of the user who created this note.
    """

    mastercard_action_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of mastercard action being refunded.
    """

    reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    The reason of the refund. Can be REFUND_EXPIRED_TRANSACTION, REFUND_REQUESTED, REFUND_MERCHANT, REFUND_CHARGEBACK.
    """

    reference_mastercard_action_event: typing.Optional[typing.List[MasterCardActionReference]] = pydantic.Field(
        default=None
    )
    """
    The reference to the object this refund applies to.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the refunded mastercard action. Can be AUTO_APPROVED, AUTO_APPROVED_WAITING_FOR_EXPIRY, PENDING_APPROVAL, APPROVED, REFUNDED, DENIED or FAILED
    """

    status_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the refund's current status.
    """

    status_description_translated: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the refund's current status, translated in user's language.
    """

    status_together_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Together topic concerning the refund's current status.
    """

    sub_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The sub type of this refund indicating whether the chargeback will be FULL or PARTIAL.
    """

    terms_and_conditions: typing.Optional[str] = pydantic.Field(default=None)
    """
    Proof that the user acknowledged the terms and conditions for chargebacks.
    """

    time_refund: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time the refund will take place.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of this refund. Can de REFUND or CHARGEBACK
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the refund's last update.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
