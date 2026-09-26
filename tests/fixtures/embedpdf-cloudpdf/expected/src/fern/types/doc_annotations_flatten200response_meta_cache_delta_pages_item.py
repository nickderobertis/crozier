

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_flatten200response_meta_cache_delta_pages_item_cache import (
    DocAnnotationsFlatten200ResponseMetaCacheDeltaPagesItemCache,
)
from .doc_annotations_flatten200response_meta_cache_delta_pages_item_page import (
    DocAnnotationsFlatten200ResponseMetaCacheDeltaPagesItemPage,
)


class DocAnnotationsFlatten200ResponseMetaCacheDeltaPagesItem(UniversalBaseModel):
    page: DocAnnotationsFlatten200ResponseMetaCacheDeltaPagesItemPage
    cache: DocAnnotationsFlatten200ResponseMetaCacheDeltaPagesItemCache

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
