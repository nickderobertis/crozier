

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .guild_product_purchase_response import GuildProductPurchaseResponse
from .purchase_type import PurchaseType


class PurchaseNotificationResponse(UniversalBaseModel):
    type: PurchaseType
    guild_product_purchase: typing.Optional[GuildProductPurchaseResponse] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
