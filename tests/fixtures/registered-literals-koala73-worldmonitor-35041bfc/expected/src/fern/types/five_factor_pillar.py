

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .excluded_bloc_member import ExcludedBlocMember
from .scorecard_evidence import ScorecardEvidence
from .scorecard_member_weight import ScorecardMemberWeight


class FiveFactorPillar(UniversalBaseModel):
    pillar: str
    has_score: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="hasScore"),
        pydantic.Field(
            alias="hasScore",
            description="Read before score and sub_score. When false, both numeric zeros are protobuf placeholders for insufficient data.",
        ),
    ]
    """
    Read before score and sub_score. When false, both numeric zeros are protobuf placeholders for insufficient data.
    """

    score: int
    sub_score: typing_extensions.Annotated[float, FieldMetadata(alias="subScore"), pydantic.Field(alias="subScore")]
    band: str
    input_coverage: typing_extensions.Annotated[
        float, FieldMetadata(alias="inputCoverage"), pydantic.Field(alias="inputCoverage")
    ]
    aggregation_method: typing_extensions.Annotated[
        str, FieldMetadata(alias="aggregationMethod"), pydantic.Field(alias="aggregationMethod")
    ]
    inputs: typing.List[ScorecardEvidence]
    insufficient_reasons: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="insufficientReasons"), pydantic.Field(alias="insufficientReasons")
    ]
    included_members: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="includedMembers"), pydantic.Field(alias="includedMembers")
    ]
    excluded_members: typing_extensions.Annotated[
        typing.List[ExcludedBlocMember], FieldMetadata(alias="excludedMembers"), pydantic.Field(alias="excludedMembers")
    ]
    member_weights: typing_extensions.Annotated[
        typing.List[ScorecardMemberWeight], FieldMetadata(alias="memberWeights"), pydantic.Field(alias="memberWeights")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
