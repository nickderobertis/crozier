

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .feature import Feature
from .page_metadata_with_total import PageMetadataWithTotal


class FeaturePage(UniversalBaseModel):
    metadata: PageMetadataWithTotal
    data: typing.List[Feature]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
