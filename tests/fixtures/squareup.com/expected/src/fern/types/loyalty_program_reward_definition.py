

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .money import Money


class LoyaltyProgramRewardDefinition(UniversalBaseModel):
    """
    Provides details about the reward tier discount. DEPRECATED at version 2020-12-16. Discount details
    are now defined using a catalog pricing rule and other catalog objects. For more information, see
    [Get discount details for the reward](https://developer.squareup.com/docs/loyalty-api/overview#get-discount-details).
    """

    catalog_object_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The list of catalog objects to which this reward can be applied. They are either all item-variation ids or category ids, depending on the `type` field.
    DEPRECATED at version 2020-12-16. You can find this information in the `product_set_data.product_ids_any` field
    of the `PRODUCT_SET` catalog object referenced by the pricing rule.
    """

    discount_type: str = pydantic.Field()
    """
    The type of discount the reward tier offers. DEPRECATED at version 2020-12-16. You can find this information
    in the `discount_data.discount_type` field of the `DISCOUNT` catalog object referenced by the pricing rule.
    """

    fixed_discount_money: typing.Optional[Money] = None
    max_discount_money: typing.Optional[Money] = None
    percentage_discount: typing.Optional[str] = pydantic.Field(default=None)
    """
    The fixed percentage of the discount. Present if `discount_type` is `FIXED_PERCENTAGE`.
    For example, a 7.25% off discount will be represented as "7.25". DEPRECATED at version 2020-12-16. You can find this
    information in the `discount_data.percentage` field of the `DISCOUNT` catalog object referenced by the pricing rule.
    """

    scope: str = pydantic.Field()
    """
    Indicates the scope of the reward tier. DEPRECATED at version 2020-12-16. You can find this information in the
    `discount_target_scope` field of the `PRICING_RULE` catalog object and the `product_set_data` field of the `PRODUCT_SET`
    catalog object referenced by the pricing rule. For `ORDER` scopes, the target scope is `WHOLE_PURCHASE` and `all_products`
    is true. For `ITEM_VARIATION` and `CATEGORY` scopes, the target scope is `LINE_ITEM` and `product_ids_any` is a list of
    catalog object IDs of the given type.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
