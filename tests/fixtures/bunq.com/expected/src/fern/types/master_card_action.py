

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amount import Amount
from .label_card import LabelCard
from .label_monetary_account import LabelMonetaryAccount
from .master_card_action_refund import MasterCardActionRefund
from .request_inquiry_reference import RequestInquiryReference


class MasterCardAction(UniversalBaseModel):
    alias: typing.Optional[LabelMonetaryAccount] = pydantic.Field(default=None)
    """
    The monetary account label of the account that this action is created for.
    """

    all_mastercard_action_refund: typing.Optional[typing.List[MasterCardActionRefund]] = pydantic.Field(default=None)
    """
    A reference to the Refunds if they exist.
    """

    amount_billing: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The amount of the transaction in the monetary account's currency.
    """

    amount_converted: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The amount of the transaction in local currency.
    """

    amount_fee: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The fee amount as charged by the merchant, if applicable.
    """

    amount_local: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The amount of the transaction in local currency.
    """

    amount_original_billing: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The original amount in the monetary account's currency.
    """

    amount_original_local: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The original amount in local currency.
    """

    applied_limit: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of the limit applied to validate if this MasterCardAction was within the spending limits. The returned string matches the limit types as defined in the card endpoint.
    """

    authorisation_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status in the authorisation process.
    """

    authorisation_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of transaction that was delivered using the card.
    """

    card_authorisation_id_response: typing.Optional[str] = pydantic.Field(default=None)
    """
    The response code by which authorised transaction can be identified as authorised by bunq.
    """

    card_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the card this action links to.
    """

    city: typing.Optional[str] = pydantic.Field(default=None)
    """
    The city where the message originates from as announced by the terminal.
    """

    clearing_expiry_time: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time when the processing of the clearing is expired, refunding the authorisation.
    """

    clearing_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The clearing status of the authorisation. Can be 'PENDING', 'FIRST_PRESENTMENT_COMPLETE' or 'REFUND_LENIENCY'.
    """

    counterparty_alias: typing.Optional[LabelMonetaryAccount] = pydantic.Field(default=None)
    """
    The monetary account label of the counterparty.
    """

    decision: typing.Optional[str] = pydantic.Field(default=None)
    """
    Why the transaction was denied, if it was denied, or just ALLOWED.
    """

    decision_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Empty if allowed, otherwise a textual explanation of why it was denied.
    """

    decision_description_translated: typing.Optional[str] = pydantic.Field(default=None)
    """
    Empty if allowed, otherwise a textual explanation of why it was denied in user's language.
    """

    decision_together_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Empty if allowed or if no relevant Together topic exists, otherwise contains the URL for a Together topic with more information about the decision.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description for this transaction to display.
    """

    eligible_whitelist_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The whitelist id for this action or null.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the MastercardAction.
    """

    label_card: typing.Optional[LabelCard] = pydantic.Field(default=None)
    """
    The label of the card.
    """

    maturity_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    The maturity date.
    """

    monetary_account_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the monetary account this action links to.
    """

    pan_entry_mode_user: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of entry mode the user used. Can be 'ATM', 'ICC', 'MAGNETIC_STRIPE' or 'E_COMMERCE'.
    """

    payment_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The payment status of the transaction. For example PAYMENT_SUCCESSFUL, for a successful payment.
    """

    pos_card_holder_presence: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Card Holder Presence type of the POS.
    """

    pos_card_presence: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Card Presence type of the POS.
    """

    request_reference_split_the_bill: typing.Optional[typing.List[RequestInquiryReference]] = pydantic.Field(
        default=None
    )
    """
    The reference to the object used for split the bill. Can be RequestInquiry or RequestInquiryBatch
    """

    reservation_expiry_time: typing.Optional[str] = pydantic.Field(default=None)
    """
    If this is a reservation, the moment the reservation will expire.
    """

    secure_code_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The secure code id for this mastercard action or null.
    """

    settlement_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The setlement status in the authorisation process.
    """

    token_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    If this is a tokenisation action, this shows the status of the token.
    """

    wallet_provider_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the wallet provider as defined by MasterCard. 420 = bunq Android app with Tap&Pay; 103 = Apple Pay.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
