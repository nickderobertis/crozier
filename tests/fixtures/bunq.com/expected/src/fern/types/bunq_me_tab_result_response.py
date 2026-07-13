

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class BunqMeTabResultResponse(UniversalBaseModel):
    payment: typing.Optional["Payment"] = pydantic.Field(default=None)
    """
    The payment made for the bunq.me tab.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .payment import Payment

update_forward_refs(BunqMeTabResultResponse)
