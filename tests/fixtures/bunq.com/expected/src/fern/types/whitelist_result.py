

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .error import Error
from .request_inquiry_reference import RequestInquiryReference
from .whitelist import Whitelist
from .whitelist_result_view_anchored_object import WhitelistResultViewAnchoredObject


class WhitelistResult(UniversalBaseModel):
    error_message: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    The message when the whitelist result has failed due to user error.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the whitelist entry.
    """

    monetary_account_paying_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The account from which payments will be deducted when a transaction is matched with this whitelist.
    """

    object: typing.Optional[WhitelistResultViewAnchoredObject] = pydantic.Field(default=None)
    """
    The details of the external object the event was created for.
    """

    request_reference_split_the_bill: typing.Optional[typing.List[RequestInquiryReference]] = pydantic.Field(
        default=None
    )
    """
    The reference to the object used for split the bill. Can be RequestInquiry or RequestInquiryBatch
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the WhitelistResult.
    """

    sub_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The subStatus of the WhitelistResult.
    """

    whitelist: typing.Optional[Whitelist] = pydantic.Field(default=None)
    """
    The corresponding whitelist.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(WhitelistResult)
