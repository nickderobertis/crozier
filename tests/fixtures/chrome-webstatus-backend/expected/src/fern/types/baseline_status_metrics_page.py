

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .baseline_status_metric import BaselineStatusMetric
from .page_metadata import PageMetadata


class BaselineStatusMetricsPage(UniversalBaseModel):
    metadata: typing.Optional[PageMetadata] = None
    data: typing.List[BaselineStatusMetric]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
