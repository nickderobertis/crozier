

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ContextWhatsappReferredProduct(UniversalBaseModel):
    """
    An object containing details of a product from a `product` message being quoted or replied to using the 'Message Business' option.
    """

    catalog_id: str = pydantic.Field()
    """
    The ID of the catalog associated with the product from the `product` message being quoted or replied to using the 'Message Business' option.
    """

    product_retailer_id: str = pydantic.Field()
    """
    The ID of the product from the `product` message being quoted or replied to using the 'Message Business' option.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
