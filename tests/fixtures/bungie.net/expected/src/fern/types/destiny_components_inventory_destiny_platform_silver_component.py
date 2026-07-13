

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_entities_items_destiny_item_component import DestinyEntitiesItemsDestinyItemComponent


class DestinyComponentsInventoryDestinyPlatformSilverComponent(UniversalBaseModel):
    platform_silver: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, DestinyEntitiesItemsDestinyItemComponent]],
        FieldMetadata(alias="platformSilver"),
    ] = pydantic.Field(default=None)
    """
    If a Profile is played on multiple platforms, this is the silver they have for each platform, keyed by Membership Type.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
