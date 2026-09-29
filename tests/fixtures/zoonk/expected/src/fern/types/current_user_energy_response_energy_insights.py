

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CurrentUserEnergyResponseEnergyInsights(UniversalBaseModel):
    average_energy: typing_extensions.Annotated[
        float, FieldMetadata(alias="averageEnergy"), pydantic.Field(alias="averageEnergy")
    ]
    full_energy_days: typing_extensions.Annotated[
        int, FieldMetadata(alias="fullEnergyDays"), pydantic.Field(alias="fullEnergyDays")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
