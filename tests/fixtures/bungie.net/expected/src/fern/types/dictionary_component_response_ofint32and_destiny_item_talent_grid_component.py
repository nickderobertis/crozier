

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .destiny_entities_items_destiny_item_talent_grid_component import (
    DestinyEntitiesItemsDestinyItemTalentGridComponent,
)


class DictionaryComponentResponseOfint32AndDestinyItemTalentGridComponent(UniversalBaseModel):
    data: typing.Optional[typing.Dict[str, DestinyEntitiesItemsDestinyItemTalentGridComponent]] = None
    disabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, this component is disabled.
    """

    privacy: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
