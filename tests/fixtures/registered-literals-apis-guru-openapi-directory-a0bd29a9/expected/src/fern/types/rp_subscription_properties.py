

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .string_string_key_value_pair import StringStringKeyValuePair
from .subscription_account_owner import SubscriptionAccountOwner
from .subscription_additional_properties import SubscriptionAdditionalProperties


class RpSubscriptionProperties(UniversalBaseModel):
    account_owner: typing_extensions.Annotated[
        typing.Optional[SubscriptionAccountOwner],
        FieldMetadata(alias="accountOwner"),
        pydantic.Field(alias="accountOwner"),
    ] = None
    additional_properties: typing_extensions.Annotated[
        typing.Optional[SubscriptionAdditionalProperties],
        FieldMetadata(alias="additionalProperties"),
        pydantic.Field(alias="additionalProperties"),
    ] = None
    location_placement_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="locationPlacementId"), pydantic.Field(alias="locationPlacementId")
    ] = None
    managed_by_tenants: typing_extensions.Annotated[
        typing.Optional[typing.List[StringStringKeyValuePair]],
        FieldMetadata(alias="managedByTenants"),
        pydantic.Field(alias="managedByTenants"),
    ] = None
    quota_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="quotaId"), pydantic.Field(alias="quotaId")
    ] = None
    registered_features: typing_extensions.Annotated[
        typing.Optional[typing.List[StringStringKeyValuePair]],
        FieldMetadata(alias="registeredFeatures"),
        pydantic.Field(alias="registeredFeatures"),
    ] = None
    tenant_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tenantId"), pydantic.Field(alias="tenantId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
