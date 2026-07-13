

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_components_loadouts_destiny_loadout_item_component import (
    DestinyComponentsLoadoutsDestinyLoadoutItemComponent,
)


class DestinyComponentsLoadoutsDestinyLoadoutComponent(UniversalBaseModel):
    color_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="colorHash")] = None
    icon_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="iconHash")] = None
    items: typing.Optional[typing.List[DestinyComponentsLoadoutsDestinyLoadoutItemComponent]] = None
    name_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="nameHash")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
