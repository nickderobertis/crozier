

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_pages_insert_blank200response_meta_cache_delta_pages_item_cache import (
    DocPagesInsertBlank200ResponseMetaCacheDeltaPagesItemCache,
)
from .doc_pages_insert_blank200response_meta_cache_delta_pages_item_page import (
    DocPagesInsertBlank200ResponseMetaCacheDeltaPagesItemPage,
)


class DocPagesInsertBlank200ResponseMetaCacheDeltaPagesItem(UniversalBaseModel):
    page: DocPagesInsertBlank200ResponseMetaCacheDeltaPagesItemPage
    cache: DocPagesInsertBlank200ResponseMetaCacheDeltaPagesItemCache

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
