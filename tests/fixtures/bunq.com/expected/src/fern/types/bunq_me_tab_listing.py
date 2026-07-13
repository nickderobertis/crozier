

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .bunq_me_tab_entry import BunqMeTabEntry
from .bunq_me_tab_result_inquiry import BunqMeTabResultInquiry
from .label_monetary_account import LabelMonetaryAccount


class BunqMeTabListing(UniversalBaseModel):
    alias_monetary_account: typing.Optional[LabelMonetaryAccount] = pydantic.Field(default=None)
    """
    The LabelMonetaryAccount with the public information of the User and the MonetaryAccount that created the bunq.me link.
    """

    bunqme_tab_entries: typing.Optional[typing.List[BunqMeTabEntry]] = pydantic.Field(default=None)
    """
    The bunq.me tab entries attached to this bunq.me Tab.
    """

    bunqme_tab_entry: typing.Optional[BunqMeTabEntry] = pydantic.Field(default=None)
    """
    The bunq.me entry containing the payment information.
    """

    bunqme_tab_share_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The url that points to the bunq.me page.
    """

    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the bunq.me was created.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the created bunq.me.
    """

    monetary_account_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the MonetaryAccount the bunq.me was sent from.
    """

    result_inquiries: typing.Optional[typing.List[BunqMeTabResultInquiry]] = pydantic.Field(default=None)
    """
    The list of bunq.me result Inquiries successfully made and paid.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the bunq.me. Can be WAITING_FOR_PAYMENT, CANCELLED or EXPIRED.
    """

    time_expiry: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of when the bunq.me expired or will expire.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of the bunq.me Tab. Should be BUNQ_ME
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the bunq.me was last updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(BunqMeTabListing)
