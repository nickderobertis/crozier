

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ScorecardMemberWeight(UniversalBaseModel):
    country_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="countryCode"), pydantic.Field(alias="countryCode")
    ]
    population_millions: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="populationMillions"),
        pydantic.Field(
            alias="populationMillions", description="Population in millions used by population-weighted components."
        ),
    ]
    """
    Population in millions used by population-weighted components.
    """

    has_population: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="hasPopulation"),
        pydantic.Field(
            alias="hasPopulation",
            description="Read before population_millions; false means the numeric zero is a placeholder.",
        ),
    ]
    """
    Read before population_millions; false means the numeric zero is a placeholder.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
