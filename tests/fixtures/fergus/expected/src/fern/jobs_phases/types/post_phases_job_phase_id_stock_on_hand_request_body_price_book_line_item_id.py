

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostPhasesJobPhaseIdStockOnHandRequestBodyPriceBookLineItemId(UniversalBaseModel):
    item_quantity: typing_extensions.Annotated[
        float, FieldMetadata(alias="itemQuantity"), pydantic.Field(alias="itemQuantity")
    ]
    price_book_line_item_id: typing_extensions.Annotated[
        float, FieldMetadata(alias="priceBookLineItemId"), pydantic.Field(alias="priceBookLineItemId")
    ]
    sales_account_id: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="salesAccountId"), pydantic.Field(alias="salesAccountId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
