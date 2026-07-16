

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .money import Money


class GiftCardActivityImport(UniversalBaseModel):
    """
    Describes a gift card activity of the IMPORT type and the `GiftCardGANSource` is OTHER
    (a third-party gift card).
    """

    amount_money: Money

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
