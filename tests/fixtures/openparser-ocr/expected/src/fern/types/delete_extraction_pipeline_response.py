

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .extraction_pipeline_id import ExtractionPipelineId


class DeleteExtractionPipelineResponse(UniversalBaseModel):
    """
    Soft-delete acknowledgement.
    """

    deleted: bool
    id: ExtractionPipelineId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
