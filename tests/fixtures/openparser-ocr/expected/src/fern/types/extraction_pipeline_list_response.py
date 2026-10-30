

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .extraction_pipeline import ExtractionPipeline


class ExtractionPipelineListResponse(UniversalBaseModel):
    """
    Active pipelines for the authenticated tenant.
    """

    items: typing.List[ExtractionPipeline]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
