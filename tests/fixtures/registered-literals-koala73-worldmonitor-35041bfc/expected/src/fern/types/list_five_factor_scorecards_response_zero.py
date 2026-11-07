

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .list_five_factor_scorecards_response_zero_methodology_version import (
    ListFiveFactorScorecardsResponseZeroMethodologyVersion,
)
from .list_five_factor_scorecards_response_zero_unavailable_reason import (
    ListFiveFactorScorecardsResponseZeroUnavailableReason,
)


class ListFiveFactorScorecardsResponseZero(UniversalBaseModel):
    unavailable: typing.Optional[str] = None
    unavailable_reason: typing_extensions.Annotated[
        typing.Optional[ListFiveFactorScorecardsResponseZeroUnavailableReason],
        FieldMetadata(alias="unavailableReason"),
        pydantic.Field(alias="unavailableReason"),
    ] = None
    methodology_version: typing_extensions.Annotated[
        typing.Optional[ListFiveFactorScorecardsResponseZeroMethodologyVersion],
        FieldMetadata(alias="methodologyVersion"),
        pydantic.Field(alias="methodologyVersion"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
