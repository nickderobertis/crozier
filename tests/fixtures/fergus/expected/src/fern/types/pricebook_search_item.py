

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .links import Links


class PricebookSearchItem(UniversalBaseModel):
    id: float = pydantic.Field()
    """
    Unique identifier for the pricebook item
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Product or item name
    """

    product_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="productCode"),
        pydantic.Field(alias="productCode", description="Product identification code"),
    ] = None
    """
    Product identification code
    """

    price_book_id: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="priceBookId"),
        pydantic.Field(alias="priceBookId", description="ID of the pricebook this item belongs to"),
    ] = None
    """
    ID of the pricebook this item belongs to
    """

    sales_account_id: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="salesAccountId"),
        pydantic.Field(alias="salesAccountId", description="Sales account ID associated with this item"),
    ] = None
    """
    Sales account ID associated with this item
    """

    unit_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="unitType"),
        pydantic.Field(alias="unitType", description="Unit of measure (e.g., 'each', 'm', 'kg')"),
    ] = None
    """
    Unit of measure (e.g., 'each', 'm', 'kg')
    """

    cost_price: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="costPrice"),
        pydantic.Field(
            alias="costPrice",
            description="Cost price of the item (price paid to supplier). Price shown is for the selected pricing tier or default tier",
        ),
    ]
    """
    Cost price of the item (price paid to supplier). Price shown is for the selected pricing tier or default tier
    """

    retail_price: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="retailPrice"),
        pydantic.Field(
            alias="retailPrice",
            description="Retail/selling price of the item. Price shown is for the selected pricing tier or default tier",
        ),
    ]
    """
    Retail/selling price of the item. Price shown is for the selected pricing tier or default tier
    """

    search_values: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="searchValues"),
        pydantic.Field(alias="searchValues", description="Concatenated searchable values used for search ranking"),
    ] = None
    """
    Concatenated searchable values used for search ranking
    """

    updated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="Timestamp of when the item was last updated"),
    ] = None
    """
    Timestamp of when the item was last updated
    """

    supplier_sku: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="supplierSku"),
        pydantic.Field(alias="supplierSku", description="Supplier's SKU or part number"),
    ] = None
    """
    Supplier's SKU or part number
    """

    links: typing.List[Links]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
