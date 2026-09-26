

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_pages_remove_name200response_meta_cache_delta_pages_item_cache import (
    DocPagesRemoveName200ResponseMetaCacheDeltaPagesItemCache,
)
from .doc_pages_remove_name200response_meta_cache_delta_pages_item_page import (
    DocPagesRemoveName200ResponseMetaCacheDeltaPagesItemPage,
)


class DocPagesRemoveName200ResponseMetaCacheDeltaPagesItem(UniversalBaseModel):
    page: DocPagesRemoveName200ResponseMetaCacheDeltaPagesItemPage
    cache: DocPagesRemoveName200ResponseMetaCacheDeltaPagesItemCache

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
