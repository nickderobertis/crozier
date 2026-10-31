

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .missing_one_impl_feature import MissingOneImplFeature
from .page_metadata import PageMetadata


class MissingOneImplFeaturesPage(UniversalBaseModel):
    metadata: typing.Optional[PageMetadata] = None
    data: typing.List[MissingOneImplFeature]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
