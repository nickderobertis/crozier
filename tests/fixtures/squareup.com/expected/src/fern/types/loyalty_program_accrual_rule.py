

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .money import Money


class LoyaltyProgramAccrualRule(UniversalBaseModel):
    """
    Defines an accrual rule, which is how buyers can earn points.
    """

    accrual_type: str = pydantic.Field()
    """
    The type of the accrual rule that defines how buyers can earn points.
    """

    catalog_object_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    When the accrual rule is item-based or category-based, this field specifies the ID 
    of the [catalog object](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) that buyers can purchase to earn points. 
    If `accrual_type` is `ITEM_VARIATION`, the object is an item variation. 
    If `accrual_type` is `CATEGORY`, the object is a category.
    """

    excluded_category_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    When the accrual rule is spend-based (`accrual_type` is `SPEND`), this field 
    lists the IDs of any `CATEGORY` catalog objects that are excluded from points accrual. 
    
    You can use the [BatchRetrieveCatalogObjects](https://developer.squareup.com/reference/square_2021-08-18/catalog-api/batch-retrieve-catalog-objects) 
    endpoint to retrieve information about the excluded categories.
    """

    excluded_item_variation_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    When the accrual rule is spend-based (`accrual_type` is `SPEND`), this field 
    lists the IDs of any `ITEM_VARIATION` catalog objects that are excluded from points accrual. 
    
    You can use the [BatchRetrieveCatalogObjects](https://developer.squareup.com/reference/square_2021-08-18/catalog-api/batch-retrieve-catalog-objects) 
    endpoint to retrieve information about the excluded item variations.
    """

    points: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of points that 
    buyers earn based on the `accrual_type`.
    """

    spend_amount_money: typing.Optional[Money] = None
    visit_minimum_amount_money: typing.Optional[Money] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
