

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FavouritesSectionLineItemsItem(UniversalBaseModel):
    id: float
    item_name: typing_extensions.Annotated[str, FieldMetadata(alias="itemName"), pydantic.Field(alias="itemName")]
    item_quantity: typing_extensions.Annotated[
        float, FieldMetadata(alias="itemQuantity"), pydantic.Field(alias="itemQuantity")
    ]
    item_cost: typing_extensions.Annotated[float, FieldMetadata(alias="itemCost"), pydantic.Field(alias="itemCost")]
    sort_order: typing_extensions.Annotated[float, FieldMetadata(alias="sortOrder"), pydantic.Field(alias="sortOrder")]
    sales_account_id: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="salesAccountId"), pydantic.Field(alias="salesAccountId")
    ] = None
    price_book_line_item_id: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="priceBookLineItemId"), pydantic.Field(alias="priceBookLineItemId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
