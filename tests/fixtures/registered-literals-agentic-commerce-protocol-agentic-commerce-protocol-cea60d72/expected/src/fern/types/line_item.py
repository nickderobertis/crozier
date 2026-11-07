

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .custom_attribute import CustomAttribute
from .disclosure import Disclosure
from .item import Item
from .marketplace_seller_details import MarketplaceSellerDetails


class LineItem(UniversalBaseModel):
    id: str
    item: Item
    base_amount: int
    discount: int
    subtotal: int
    tax: int
    total: int
    name: typing.Optional[str] = None
    description: typing.Optional[str] = None
    images: typing.Optional[typing.List[str]] = None
    unit_amount: typing.Optional[int] = None
    disclosures: typing.Optional[typing.List[Disclosure]] = None
    custom_attributes: typing.Optional[typing.List[CustomAttribute]] = None
    marketplace_seller_details: typing.Optional[MarketplaceSellerDetails] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
