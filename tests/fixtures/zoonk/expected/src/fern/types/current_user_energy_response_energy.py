

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .current_user_energy_response_energy_days_item import CurrentUserEnergyResponseEnergyDaysItem
from .current_user_energy_response_energy_insights import CurrentUserEnergyResponseEnergyInsights


class CurrentUserEnergyResponseEnergy(UniversalBaseModel):
    current_energy: typing_extensions.Annotated[
        float, FieldMetadata(alias="currentEnergy"), pydantic.Field(alias="currentEnergy")
    ]
    days: typing.List[CurrentUserEnergyResponseEnergyDaysItem]
    insights: typing.Optional[CurrentUserEnergyResponseEnergyInsights] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
