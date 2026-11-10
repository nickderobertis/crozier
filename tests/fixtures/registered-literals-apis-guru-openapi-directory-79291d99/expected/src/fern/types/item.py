

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .item_update_type import ItemUpdateType
from .plaid_error import PlaidError
from .products import Products


class Item(UniversalBaseModel):
    """
    Metadata about the Item.
    """

    available_products: typing.List[Products] = pydantic.Field()
    """
    A list of products available for the Item that have not yet been accessed. The contents of this array will be mutually exclusive with `billed_products`.
    """

    billed_products: typing.List[Products] = pydantic.Field()
    """
    A list of products that have been billed for the Item. The contents of this array will be mutually exclusive with `available_products`. Note - `billed_products` is populated in all environments but only requests in Production are billed. Also note that products that are billed on a pay-per-call basis rather than a pay-per-Item basis, such as `balance`, will not appear here.
    """

    consent_expiration_time: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The RFC 3339 timestamp after which the consent provided by the end user will expire. Upon consent expiration, the item will enter the `ITEM_LOGIN_REQUIRED` error state. To circumvent the `ITEM_LOGIN_REQUIRED` error and maintain continuous consent, the end user can reauthenticate via Link’s update mode in advance of the consent expiration time.
    
    Note - This is only relevant for certain OAuth-based institutions. For all other institutions, this field will be null.
    """

    consented_products: typing.Optional[typing.List[Products]] = pydantic.Field(default=None)
    """
    Beta: A list of products that have gone through consent collection for the Item. Only present for those enabled in the beta.
    """

    error: typing.Optional[PlaidError] = None
    institution_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Plaid Institution ID associated with the Item. Field is `null` for Items created via Same Day Micro-deposits.
    """

    item_id: str = pydantic.Field()
    """
    The Plaid Item ID. The `item_id` is always unique; linking the same account at the same institution twice will result in two Items with different `item_id` values. Like all Plaid identifiers, the `item_id` is case-sensitive.
    """

    products: typing.Optional[typing.List[Products]] = pydantic.Field(default=None)
    """
    A list of authorized products for the Item.
    """

    update_type: ItemUpdateType = pydantic.Field()
    """
    Indicates whether an Item requires user interaction to be updated, which can be the case for Items with some forms of two-factor authentication.
    
    `background` - Item can be updated in the background
    
    `user_present_required` - Item requires user interaction to be updated
    """

    webhook: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL registered to receive webhooks for the Item.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
