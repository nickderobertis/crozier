

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dictionary_component_response_ofint32and_destiny_item_objectives_component import (
    DictionaryComponentResponseOfint32AndDestinyItemObjectivesComponent,
)
from .dictionary_component_response_ofint32and_destiny_item_perks_component import (
    DictionaryComponentResponseOfint32AndDestinyItemPerksComponent,
)


class DestinyBaseItemComponentSetOfint32(UniversalBaseModel):
    objectives: typing.Optional[DictionaryComponentResponseOfint32AndDestinyItemObjectivesComponent] = None
    perks: typing.Optional[DictionaryComponentResponseOfint32AndDestinyItemPerksComponent] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
