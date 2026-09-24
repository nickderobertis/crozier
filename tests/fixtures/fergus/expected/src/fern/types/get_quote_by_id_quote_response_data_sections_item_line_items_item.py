

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GetQuoteByIdQuoteResponseDataSectionsItemLineItemsItem(UniversalBaseModel):
    quote_line_item_id: typing_extensions.Annotated[
        float, FieldMetadata(alias="quoteLineItemId"), pydantic.Field(alias="quoteLineItemId")
    ]
    price_book_line_item_id: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="priceBookLineItemId"), pydantic.Field(alias="priceBookLineItemId")
    ] = None
    item_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="itemName"), pydantic.Field(alias="itemName")
    ] = None
    item_quantity: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="itemQuantity"), pydantic.Field(alias="itemQuantity")
    ] = None
    item_price: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="itemPrice"), pydantic.Field(alias="itemPrice")
    ] = None
    item_rrp: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="itemRrp"), pydantic.Field(alias="itemRrp")
    ] = None
    item_cost: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="itemCost"), pydantic.Field(alias="itemCost")
    ] = None
    sales_account_id: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="salesAccountId"), pydantic.Field(alias="salesAccountId")
    ] = None
    is_labour: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isLabour"), pydantic.Field(alias="isLabour")
    ] = None
    sort_order: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="sortOrder"), pydantic.Field(alias="sortOrder")
    ] = None
    discount_rate: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="discountRate"), pydantic.Field(alias="discountRate")
    ] = None
    is_combined: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isCombined"), pydantic.Field(alias="isCombined")
    ] = None
    combined_item_id: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="combinedItemId"), pydantic.Field(alias="combinedItemId")
    ] = None
    combined_item_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="combinedItemName"), pydantic.Field(alias="combinedItemName")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
