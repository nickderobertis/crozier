

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .browser_release_feature_metric import BrowserReleaseFeatureMetric
from .page_metadata import PageMetadata


class BrowserReleaseFeatureMetricsPage(UniversalBaseModel):
    metadata: typing.Optional[PageMetadata] = None
    data: typing.List[BrowserReleaseFeatureMetric]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
