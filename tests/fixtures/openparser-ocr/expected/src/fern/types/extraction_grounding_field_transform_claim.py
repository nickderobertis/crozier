

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .extraction_grounding_field_transform_claim_confidence import ExtractionGroundingFieldTransformClaimConfidence
from .extraction_grounding_field_transform_claim_operation import ExtractionGroundingFieldTransformClaimOperation
from .extraction_grounding_field_transform_claim_parameters_value import (
    ExtractionGroundingFieldTransformClaimParametersValue,
)


class ExtractionGroundingFieldTransformClaim(UniversalBaseModel):
    """
    The model's bounded report of a rewrite: operation, parameters, reason, and optional
    low/medium/high ordinal confidence. The claim is untrusted and never authorizes a
    deterministic validator; only explicit request/schema intent can do that.
    """

    operation: ExtractionGroundingFieldTransformClaimOperation
    parameters: typing.Dict[str, ExtractionGroundingFieldTransformClaimParametersValue]
    reason: str
    confidence: typing.Optional[ExtractionGroundingFieldTransformClaimConfidence] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
