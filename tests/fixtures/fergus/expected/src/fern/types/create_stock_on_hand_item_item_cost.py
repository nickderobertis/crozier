

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CreateStockOnHandItemItemCost(UniversalBaseModel):
    item_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="itemDescription"), pydantic.Field(alias="itemDescription")
    ]
    item_price: typing_extensions.Annotated[float, FieldMetadata(alias="itemPrice"), pydantic.Field(alias="itemPrice")]
    item_cost: typing_extensions.Annotated[float, FieldMetadata(alias="itemCost"), pydantic.Field(alias="itemCost")]
    item_quantity: typing_extensions.Annotated[
        float, FieldMetadata(alias="itemQuantity"), pydantic.Field(alias="itemQuantity")
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
