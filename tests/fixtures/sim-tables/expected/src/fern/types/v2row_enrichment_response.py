

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2enrichment_run_detail import V2EnrichmentRunDetail


class V2RowEnrichmentResponse(UniversalBaseModel):
    """
    Provider cascade, cost, and timing for one enrichment cell.
    """

    data: typing.Optional[V2EnrichmentRunDetail] = pydantic.Field(default=None)
    """
    Response data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
