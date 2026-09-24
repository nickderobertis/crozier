

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .links import Links
from .pricebook_item_pricing_tier import PricebookItemPricingTier


class PricebookItem(UniversalBaseModel):
    id: float
    name: typing.Optional[str] = None
    product_code: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="productCode"), pydantic.Field(alias="productCode")
    ] = None
    price_book_id: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="priceBookId"), pydantic.Field(alias="priceBookId")
    ] = None
    unit_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="unitType"), pydantic.Field(alias="unitType")
    ] = None
    cost_price: typing_extensions.Annotated[float, FieldMetadata(alias="costPrice"), pydantic.Field(alias="costPrice")]
    retail_price: typing_extensions.Annotated[
        float, FieldMetadata(alias="retailPrice"), pydantic.Field(alias="retailPrice")
    ]
    search_values: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="searchValues"), pydantic.Field(alias="searchValues")
    ] = None
    updated_at: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ] = None
    supplier_sku: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="supplierSku"), pydantic.Field(alias="supplierSku")
    ] = None
    pricing_tier: typing_extensions.Annotated[
        typing.List[PricebookItemPricingTier], FieldMetadata(alias="pricingTier"), pydantic.Field(alias="pricingTier")
    ]
    links: typing.List[Links]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
