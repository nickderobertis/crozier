

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .five_factor_country_scorecard_methodology_version import FiveFactorCountryScorecardMethodologyVersion
from .five_factor_pillar import FiveFactorPillar


class FiveFactorCountryScorecard(UniversalBaseModel):
    country_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="countryCode"), pydantic.Field(alias="countryCode")
    ]
    methodology_version: typing_extensions.Annotated[
        FiveFactorCountryScorecardMethodologyVersion,
        FieldMetadata(alias="methodologyVersion"),
        pydantic.Field(alias="methodologyVersion"),
    ]
    computed_at: typing_extensions.Annotated[str, FieldMetadata(alias="computedAt"), pydantic.Field(alias="computedAt")]
    pillars: typing.List[FiveFactorPillar]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
