

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .page_metadata import PageMetadata
from .wpt_run_metric import WptRunMetric


class WptRunMetricsPage(UniversalBaseModel):
    metadata: typing.Optional[PageMetadata] = None
    data: typing.List[WptRunMetric]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
