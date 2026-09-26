

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_signatures_complete200response_meta_cache_delta_pages_item_cache import (
    DocSignaturesComplete200ResponseMetaCacheDeltaPagesItemCache,
)
from .doc_signatures_complete200response_meta_cache_delta_pages_item_page import (
    DocSignaturesComplete200ResponseMetaCacheDeltaPagesItemPage,
)


class DocSignaturesComplete200ResponseMetaCacheDeltaPagesItem(UniversalBaseModel):
    page: DocSignaturesComplete200ResponseMetaCacheDeltaPagesItemPage
    cache: DocSignaturesComplete200ResponseMetaCacheDeltaPagesItemCache

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
