

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_records_destiny_record_definition import DestinyDefinitionsRecordsDestinyRecordDefinition
from .tokens_collectible_definitions import TokensCollectibleDefinitions


class TokensRewardAvailabilityModel(UniversalBaseModel):
    collectible_definitions: typing_extensions.Annotated[
        typing.Optional[typing.List[TokensCollectibleDefinitions]], FieldMetadata(alias="CollectibleDefinitions")
    ] = None
    decrypted_token: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="DecryptedToken")] = None
    game_earn_by_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="GameEarnByDate")
    ] = None
    has_existing_code: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="HasExistingCode")] = None
    has_offer: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="HasOffer")] = None
    is_loyalty_reward: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="IsLoyaltyReward")] = None
    is_offer: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="IsOffer")] = None
    offer_applied: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="OfferApplied")] = None
    record_definitions: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsRecordsDestinyRecordDefinition]],
        FieldMetadata(alias="RecordDefinitions"),
    ] = None
    redemption_end_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="RedemptionEndDate")
    ] = None
    shopify_end_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="ShopifyEndDate")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
