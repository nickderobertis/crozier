

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .get_five_factor_scorecard_response_zero_unavailable_reason import (
    GetFiveFactorScorecardResponseZeroUnavailableReason,
)


class GetFiveFactorScorecardResponseZero(UniversalBaseModel):
    unavailable: typing.Optional[str] = None
    unavailable_reason: typing_extensions.Annotated[
        typing.Optional[GetFiveFactorScorecardResponseZeroUnavailableReason],
        FieldMetadata(alias="unavailableReason"),
        pydantic.Field(alias="unavailableReason"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
