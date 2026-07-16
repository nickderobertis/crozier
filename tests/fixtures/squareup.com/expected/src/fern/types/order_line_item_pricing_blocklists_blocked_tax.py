

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OrderLineItemPricingBlocklistsBlockedTax(UniversalBaseModel):
    """
    A tax to block from applying to a line item. The tax must be
    identified by either `tax_uid` or `tax_catalog_object_id`, but not both.
    """

    tax_catalog_object_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The `catalog_object_id` of the tax that should be blocked. 
    Use this field to block catalog taxes. For ad hoc taxes, use the 
    `tax_uid` field.
    """

    tax_uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The `uid` of the tax that should be blocked. Use this field to block 
    ad hoc taxes. For catalog, taxes use the `tax_catalog_object_id` field.
    """

    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique ID of the `BlockedTax` within the order.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
