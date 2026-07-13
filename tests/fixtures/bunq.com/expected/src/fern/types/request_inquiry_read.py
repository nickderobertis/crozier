

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .address import Address
from .amount import Amount
from .bunq_id import BunqId
from .geolocation import Geolocation
from .label_monetary_account import LabelMonetaryAccount
from .label_user import LabelUser
from .request_reference_split_the_bill_anchor_object import RequestReferenceSplitTheBillAnchorObject


class RequestInquiryRead(UniversalBaseModel):
    address_billing: typing.Optional[Address] = pydantic.Field(default=None)
    """
    The billing address provided by the accepting user if an address was requested.
    """

    address_shipping: typing.Optional[Address] = pydantic.Field(default=None)
    """
    The shipping address provided by the accepting user if an address was requested.
    """

    amount_inquired: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The requested amount.
    """

    amount_responded: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The responded amount.
    """

    attachment: typing.Optional[typing.List[BunqId]] = pydantic.Field(default=None)
    """
    The attachments attached to the payment.
    """

    batch_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the batch if the request was part of a batch.
    """

    bunqme_share_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The url that points to the bunq.me request.
    """

    counterparty_alias: typing.Optional[LabelMonetaryAccount] = pydantic.Field(default=None)
    """
    The LabelMonetaryAccount with the public information of the MonetaryAccount the money was requested from.
    """

    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the payment request's creation.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the inquiry.
    """

    geolocation: typing.Optional[Geolocation] = pydantic.Field(default=None)
    """
    The geolocation where the payment was done.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the created RequestInquiry.
    """

    merchant_reference: typing.Optional[str] = pydantic.Field(default=None)
    """
    The client's custom reference that was attached to the request and the mutation.
    """

    minimum_age: typing.Optional[int] = pydantic.Field(default=None)
    """
    The minimum age the user accepting the RequestInquiry must have.
    """

    monetary_account_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the monetary account the request response applies to.
    """

    redirect_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL which the user is sent to after accepting or rejecting the Request.
    """

    reference_split_the_bill: typing.Optional[RequestReferenceSplitTheBillAnchorObject] = pydantic.Field(default=None)
    """
    The reference to the object used for split the bill. Can be Payment, PaymentBatch, ScheduleInstance, RequestResponse and MasterCardAction
    """

    require_address: typing.Optional[str] = pydantic.Field(default=None)
    """
    Whether or not an address must be provided on accept.
    """

    scheduled_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the scheduled job if the request was scheduled.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the request.
    """

    time_expiry: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of when the payment request expired.
    """

    time_responded: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of when the payment request was responded to.
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the payment request's last update.
    """

    user_alias_created: typing.Optional[LabelUser] = pydantic.Field(default=None)
    """
    The label that's displayed to the counterparty with the mutation. Includes user.
    """

    user_alias_revoked: typing.Optional[LabelUser] = pydantic.Field(default=None)
    """
    The label that's displayed to the counterparty with the mutation. Includes user.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(RequestInquiryRead)
