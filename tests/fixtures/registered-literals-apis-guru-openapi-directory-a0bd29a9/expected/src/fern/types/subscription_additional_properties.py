

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .billing_properties import BillingProperties


class SubscriptionAdditionalProperties(UniversalBaseModel):
    billing_properties: typing_extensions.Annotated[
        typing.Optional[BillingProperties],
        FieldMetadata(alias="billingProperties"),
        pydantic.Field(alias="billingProperties"),
    ] = None
    resource_provider_properties: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="resourceProviderProperties"),
        pydantic.Field(alias="resourceProviderProperties"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
