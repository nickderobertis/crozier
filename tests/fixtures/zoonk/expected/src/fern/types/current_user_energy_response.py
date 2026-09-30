

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .current_user_energy_response_energy import CurrentUserEnergyResponseEnergy


class CurrentUserEnergyResponse(UniversalBaseModel):
    energy: typing.Optional[CurrentUserEnergyResponseEnergy] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
