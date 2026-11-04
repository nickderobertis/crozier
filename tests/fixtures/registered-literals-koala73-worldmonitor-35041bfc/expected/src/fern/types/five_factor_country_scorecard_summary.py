

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .five_factor_pillar_summary import FiveFactorPillarSummary


class FiveFactorCountryScorecardSummary(UniversalBaseModel):
    country_code: typing_extensions.Annotated[
        str, FieldMetadata(alias="countryCode"), pydantic.Field(alias="countryCode")
    ]
    pillars: typing.List[FiveFactorPillarSummary]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
