

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class StockUsedItem(UniversalBaseModel):
    product_code: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="productCode"), pydantic.Field(alias="productCode")
    ] = None
    product_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="productName"), pydantic.Field(alias="productName")
    ]
    pricebook_line_item_id: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="pricebookLineItemId"), pydantic.Field(alias="pricebookLineItemId")
    ] = None
    pricebook_id: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="pricebookId"), pydantic.Field(alias="pricebookId")
    ] = None
    total_qty: typing_extensions.Annotated[float, FieldMetadata(alias="totalQty"), pydantic.Field(alias="totalQty")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
