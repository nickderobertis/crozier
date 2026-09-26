

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_redactions_apply200response_meta_cache_delta_pages_item_cache import (
    DocRedactionsApply200ResponseMetaCacheDeltaPagesItemCache,
)
from .doc_redactions_apply200response_meta_cache_delta_pages_item_page import (
    DocRedactionsApply200ResponseMetaCacheDeltaPagesItemPage,
)


class DocRedactionsApply200ResponseMetaCacheDeltaPagesItem(UniversalBaseModel):
    page: DocRedactionsApply200ResponseMetaCacheDeltaPagesItemPage
    cache: DocRedactionsApply200ResponseMetaCacheDeltaPagesItemCache

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
