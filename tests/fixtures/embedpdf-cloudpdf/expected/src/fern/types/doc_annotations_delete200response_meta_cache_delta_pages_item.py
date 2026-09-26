

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_delete200response_meta_cache_delta_pages_item_cache import (
    DocAnnotationsDelete200ResponseMetaCacheDeltaPagesItemCache,
)
from .doc_annotations_delete200response_meta_cache_delta_pages_item_page import (
    DocAnnotationsDelete200ResponseMetaCacheDeltaPagesItemPage,
)


class DocAnnotationsDelete200ResponseMetaCacheDeltaPagesItem(UniversalBaseModel):
    page: DocAnnotationsDelete200ResponseMetaCacheDeltaPagesItemPage
    cache: DocAnnotationsDelete200ResponseMetaCacheDeltaPagesItemCache

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
