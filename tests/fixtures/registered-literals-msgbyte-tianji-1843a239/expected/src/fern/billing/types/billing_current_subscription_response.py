

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class BillingCurrentSubscriptionResponse(UniversalBaseModel):
    subscription_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="subscriptionId"), pydantic.Field(alias="subscriptionId")
    ]
    workspace_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="workspaceId"), pydantic.Field(alias="workspaceId")
    ]
    store_id: typing_extensions.Annotated[str, FieldMetadata(alias="storeId"), pydantic.Field(alias="storeId")]
    product_id: typing_extensions.Annotated[str, FieldMetadata(alias="productId"), pydantic.Field(alias="productId")]
    variant_id: typing_extensions.Annotated[str, FieldMetadata(alias="variantId"), pydantic.Field(alias="variantId")]
    status: str
    card_brand: typing_extensions.Annotated[str, FieldMetadata(alias="cardBrand"), pydantic.Field(alias="cardBrand")]
    card_last_four: typing_extensions.Annotated[
        str, FieldMetadata(alias="cardLastFour"), pydantic.Field(alias="cardLastFour")
    ]
    renews_at: typing_extensions.Annotated[str, FieldMetadata(alias="renewsAt"), pydantic.Field(alias="renewsAt")]
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    updated_at: typing_extensions.Annotated[str, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")]
    tier: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
