

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .extraction_grounding_mode import ExtractionGroundingMode
from .extraction_pipeline_id import ExtractionPipelineId
from .extraction_pipeline_llm_options import ExtractionPipelineLlmOptions
from .llm_model import LlmModel


class ExtractionPipeline(UniversalBaseModel):
    """
    Public saved extraction pipeline resource.
    """

    id: ExtractionPipelineId
    name: str
    slug: typing.Optional[str] = None
    version: int
    ocr_model: str
    ocr_options: typing.Dict[str, typing.Any]
    llm_model: LlmModel
    llm_options: ExtractionPipelineLlmOptions
    schema_: typing_extensions.Annotated[
        typing.Dict[str, typing.Any],
        FieldMetadata(alias="schema"),
        pydantic.Field(
            alias="schema",
            description="Persisted extraction schema with at least one root property. Normalized for strict\nstructured outputs at save time.",
        ),
    ]
    """
    Persisted extraction schema with at least one root property. Normalized for strict
    structured outputs at save time.
    """

    repair_attempts: int
    grounding: ExtractionGroundingMode
    created_at: dt.datetime
    updated_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
