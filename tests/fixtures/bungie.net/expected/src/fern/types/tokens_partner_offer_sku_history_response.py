

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tokens_partner_offer_history_response import TokensPartnerOfferHistoryResponse


class TokensPartnerOfferSkuHistoryResponse(UniversalBaseModel):
    all_offers_applied: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="AllOffersApplied")] = (
        None
    )
    claim_date: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="ClaimDate")] = None
    localized_description: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="LocalizedDescription")
    ] = None
    localized_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="LocalizedName")] = None
    sku_identifier: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="SkuIdentifier")] = None
    sku_offers: typing_extensions.Annotated[
        typing.Optional[typing.List[TokensPartnerOfferHistoryResponse]], FieldMetadata(alias="SkuOffers")
    ] = None
    transaction_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="TransactionId")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
