

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .insight_with_metadata import InsightWithMetadata


class GetInsightsResponse(UniversalBaseModel):
    insights: typing.List[InsightWithMetadata] = pydantic.Field()
    """
    List of insights with query counts
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
