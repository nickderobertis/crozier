

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .magic_item_rarity_name import MagicItemRarityName


class MagicItemRarity(UniversalBaseModel):
    name: typing.Optional[MagicItemRarityName] = pydantic.Field(default=None)
    """
    The rarity of the item.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
