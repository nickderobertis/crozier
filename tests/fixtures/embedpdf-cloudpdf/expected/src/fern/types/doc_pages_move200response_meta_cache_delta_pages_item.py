

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_pages_move200response_meta_cache_delta_pages_item_cache import (
    DocPagesMove200ResponseMetaCacheDeltaPagesItemCache,
)
from .doc_pages_move200response_meta_cache_delta_pages_item_page import (
    DocPagesMove200ResponseMetaCacheDeltaPagesItemPage,
)


class DocPagesMove200ResponseMetaCacheDeltaPagesItem(UniversalBaseModel):
    page: DocPagesMove200ResponseMetaCacheDeltaPagesItemPage
    cache: DocPagesMove200ResponseMetaCacheDeltaPagesItemCache

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
