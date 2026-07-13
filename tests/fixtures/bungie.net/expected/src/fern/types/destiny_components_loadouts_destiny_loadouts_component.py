

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .destiny_components_loadouts_destiny_loadout_component import DestinyComponentsLoadoutsDestinyLoadoutComponent


class DestinyComponentsLoadoutsDestinyLoadoutsComponent(UniversalBaseModel):
    loadouts: typing.Optional[typing.List[DestinyComponentsLoadoutsDestinyLoadoutComponent]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
