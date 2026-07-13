

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TokensPartnerOfferHistoryResponse(UniversalBaseModel):
    apply_date: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="ApplyDate")] = None
    is_consumable: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="IsConsumable")] = None
    localized_description: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="LocalizedDescription")
    ] = None
    localized_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="LocalizedName")] = None
    membership_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="MembershipId")] = None
    membership_type: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="MembershipType")] = None
    partner_offer_key: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="PartnerOfferKey")] = None
    quantity_applied: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="QuantityApplied")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
