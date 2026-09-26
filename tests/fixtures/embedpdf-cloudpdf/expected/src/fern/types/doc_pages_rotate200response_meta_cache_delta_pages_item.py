

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_pages_rotate200response_meta_cache_delta_pages_item_cache import (
    DocPagesRotate200ResponseMetaCacheDeltaPagesItemCache,
)
from .doc_pages_rotate200response_meta_cache_delta_pages_item_page import (
    DocPagesRotate200ResponseMetaCacheDeltaPagesItemPage,
)


class DocPagesRotate200ResponseMetaCacheDeltaPagesItem(UniversalBaseModel):
    page: DocPagesRotate200ResponseMetaCacheDeltaPagesItemPage
    cache: DocPagesRotate200ResponseMetaCacheDeltaPagesItemCache

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
