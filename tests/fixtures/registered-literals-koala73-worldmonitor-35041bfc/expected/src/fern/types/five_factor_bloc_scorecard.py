

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .excluded_bloc_member import ExcludedBlocMember
from .five_factor_bloc_scorecard_methodology_version import FiveFactorBlocScorecardMethodologyVersion
from .five_factor_pillar import FiveFactorPillar


class FiveFactorBlocScorecard(UniversalBaseModel):
    id: str
    label: str
    methodology_version: typing_extensions.Annotated[
        FiveFactorBlocScorecardMethodologyVersion,
        FieldMetadata(alias="methodologyVersion"),
        pydantic.Field(alias="methodologyVersion"),
    ]
    computed_at: typing_extensions.Annotated[str, FieldMetadata(alias="computedAt"), pydantic.Field(alias="computedAt")]
    members: typing.List[str]
    included_members: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="includedMembers"), pydantic.Field(alias="includedMembers")
    ]
    excluded_members: typing_extensions.Annotated[
        typing.List[ExcludedBlocMember], FieldMetadata(alias="excludedMembers"), pydantic.Field(alias="excludedMembers")
    ]
    pillars: typing.List[FiveFactorPillar]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
