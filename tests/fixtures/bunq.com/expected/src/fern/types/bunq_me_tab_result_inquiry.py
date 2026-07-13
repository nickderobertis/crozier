

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class BunqMeTabResultInquiry(UniversalBaseModel):
    bunq_me_tab_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The Id of the bunq.me tab that this BunqMeTabResultInquiry belongs to.
    """

    payment: typing.Optional["Payment"] = pydantic.Field(default=None)
    """
    The payment made for the Tab.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .payment import Payment

update_forward_refs(BunqMeTabResultInquiry)
