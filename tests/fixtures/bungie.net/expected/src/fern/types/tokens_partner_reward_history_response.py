

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tokens_partner_offer_sku_history_response import TokensPartnerOfferSkuHistoryResponse
from .tokens_twitch_drop_history_response import TokensTwitchDropHistoryResponse


class TokensPartnerRewardHistoryResponse(UniversalBaseModel):
    partner_offers: typing_extensions.Annotated[
        typing.Optional[typing.List[TokensPartnerOfferSkuHistoryResponse]],
        FieldMetadata(alias="PartnerOffers"),
        pydantic.Field(alias="PartnerOffers"),
    ] = None
    twitch_drops: typing_extensions.Annotated[
        typing.Optional[typing.List[TokensTwitchDropHistoryResponse]],
        FieldMetadata(alias="TwitchDrops"),
        pydantic.Field(alias="TwitchDrops"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
