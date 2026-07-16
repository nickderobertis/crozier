

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .additional_recipient import AdditionalRecipient
from .money import Money


class Refund(UniversalBaseModel):
    """
    Represents a refund processed for a Square transaction.
    """

    additional_recipients: typing.Optional[typing.List[AdditionalRecipient]] = pydantic.Field(default=None)
    """
    Additional recipients (other than the merchant) receiving a portion of this refund.
    For example, fees assessed on a refund of a purchase by a third party integration.
    """

    amount_money: Money
    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp for when the refund was created, in RFC 3339 format.
    """

    id: str = pydantic.Field()
    """
    The refund's unique ID.
    """

    location_id: str = pydantic.Field()
    """
    The ID of the refund's associated location.
    """

    processing_fee_money: typing.Optional[Money] = None
    reason: str = pydantic.Field()
    """
    The reason for the refund being issued.
    """

    status: str = pydantic.Field()
    """
    The current status of the refund (`PENDING`, `APPROVED`, `REJECTED`,
    or `FAILED`).
    """

    tender_id: str = pydantic.Field()
    """
    The ID of the refunded tender.
    """

    transaction_id: str = pydantic.Field()
    """
    The ID of the transaction that the refunded tender is part of.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
