

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FiveFactorPillarSummary(UniversalBaseModel):
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
    insufficient_reasons: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="insufficientReasons"), pydantic.Field(alias="insufficientReasons")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
