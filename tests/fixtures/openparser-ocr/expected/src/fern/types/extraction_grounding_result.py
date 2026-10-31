

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .extraction_grounding_field import ExtractionGroundingField
from .extraction_grounding_result_mode import ExtractionGroundingResultMode


class ExtractionGroundingResult(UniversalBaseModel):
    """
    Optional terminal grounding envelope present only when `grounding: field` succeeded.
    """

    mode: ExtractionGroundingResultMode
    fields: typing.List[ExtractionGroundingField]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
