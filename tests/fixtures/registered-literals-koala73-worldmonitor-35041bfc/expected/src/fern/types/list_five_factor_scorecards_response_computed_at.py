

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .list_five_factor_scorecards_response_computed_at_computed_at import (
    ListFiveFactorScorecardsResponseComputedAtComputedAt,
)
from .list_five_factor_scorecards_response_computed_at_methodology_version import (
    ListFiveFactorScorecardsResponseComputedAtMethodologyVersion,
)
from .list_five_factor_scorecards_response_computed_at_unavailable_reason import (
    ListFiveFactorScorecardsResponseComputedAtUnavailableReason,
)


class ListFiveFactorScorecardsResponseComputedAt(UniversalBaseModel):
    unavailable: typing.Optional[str] = None
    unavailable_reason: typing_extensions.Annotated[
        typing.Optional[ListFiveFactorScorecardsResponseComputedAtUnavailableReason],
        FieldMetadata(alias="unavailableReason"),
        pydantic.Field(alias="unavailableReason"),
    ] = None
    methodology_version: typing_extensions.Annotated[
        typing.Optional[ListFiveFactorScorecardsResponseComputedAtMethodologyVersion],
        FieldMetadata(alias="methodologyVersion"),
        pydantic.Field(alias="methodologyVersion"),
    ] = None
    computed_at: typing_extensions.Annotated[
        typing.Optional[ListFiveFactorScorecardsResponseComputedAtComputedAt],
        FieldMetadata(alias="computedAt"),
        pydantic.Field(alias="computedAt"),
    ] = None
    scorecards: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
