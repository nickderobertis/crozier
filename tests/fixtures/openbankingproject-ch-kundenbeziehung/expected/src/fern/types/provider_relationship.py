

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .monetary_amount import MonetaryAmount
from .provider_relationship_relationship_type import ProviderRelationshipRelationshipType


class ProviderRelationship(UniversalBaseModel):
    provider_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="providerId"), pydantic.Field(alias="providerId")
    ] = None
    relationship_type: typing_extensions.Annotated[
        typing.Optional[ProviderRelationshipRelationshipType],
        FieldMetadata(alias="relationshipType"),
        pydantic.Field(alias="relationshipType"),
    ] = None
    since: typing.Optional[dt.date] = None
    portfolio_value: typing_extensions.Annotated[
        typing.Optional[MonetaryAmount], FieldMetadata(alias="portfolioValue"), pydantic.Field(alias="portfolioValue")
    ] = None
    custody_bank: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="custodyBank"), pydantic.Field(alias="custodyBank")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
