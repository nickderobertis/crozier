

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dictionary_component_response_ofint64and_destiny_item_objectives_component import (
    DictionaryComponentResponseOfint64AndDestinyItemObjectivesComponent,
)
from .dictionary_component_response_ofint64and_destiny_item_perks_component import (
    DictionaryComponentResponseOfint64AndDestinyItemPerksComponent,
)


class DestinyBaseItemComponentSetOfint64(UniversalBaseModel):
    objectives: typing.Optional[DictionaryComponentResponseOfint64AndDestinyItemObjectivesComponent] = None
    perks: typing.Optional[DictionaryComponentResponseOfint64AndDestinyItemPerksComponent] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
