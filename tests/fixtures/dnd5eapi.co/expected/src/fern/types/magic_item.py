

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .api_reference import ApiReference
from .magic_item_rarity import MagicItemRarity
from .resource_description import ResourceDescription


class MagicItem(ApiReference, ResourceDescription):
    """
    `MagicItem`
    """

    equipment_category: typing.Optional[ApiReference] = None
    rarity: typing.Optional[MagicItemRarity] = None
    variant: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether this is a variant or not
    """

    variants: typing.Optional[typing.List[ApiReference]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
