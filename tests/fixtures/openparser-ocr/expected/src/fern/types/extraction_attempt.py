

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .extraction_attempt_kind import ExtractionAttemptKind
from .extraction_attempt_status import ExtractionAttemptStatus
from .llm_model import LlmModel


class ExtractionAttempt(UniversalBaseModel):
    index: int = pydantic.Field()
    """
    Zero-based attempt index in execution order.
    """

    kind: ExtractionAttemptKind
    llm_model: LlmModel
    status: ExtractionAttemptStatus
    input_tokens: typing.Optional[int] = None
    output_tokens: typing.Optional[int] = None
    cost_usd: typing.Optional[float] = pydantic.Field(default=None)
    """
    Customer retail USD for this attempt (OpenRouter provider cost converted to the
    rates customers are charged). Distinct from the OCR page charge.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
