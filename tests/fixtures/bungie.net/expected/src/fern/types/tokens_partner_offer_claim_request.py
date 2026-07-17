

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TokensPartnerOfferClaimRequest(UniversalBaseModel):
    bungie_net_membership_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="BungieNetMembershipId"),
        pydantic.Field(alias="BungieNetMembershipId"),
    ] = None
    partner_offer_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="PartnerOfferId"), pydantic.Field(alias="PartnerOfferId")
    ] = None
    transaction_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="TransactionId"), pydantic.Field(alias="TransactionId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
