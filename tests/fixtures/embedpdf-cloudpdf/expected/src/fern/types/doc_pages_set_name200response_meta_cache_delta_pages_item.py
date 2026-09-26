

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_pages_set_name200response_meta_cache_delta_pages_item_cache import (
    DocPagesSetName200ResponseMetaCacheDeltaPagesItemCache,
)
from .doc_pages_set_name200response_meta_cache_delta_pages_item_page import (
    DocPagesSetName200ResponseMetaCacheDeltaPagesItemPage,
)


class DocPagesSetName200ResponseMetaCacheDeltaPagesItem(UniversalBaseModel):
    page: DocPagesSetName200ResponseMetaCacheDeltaPagesItemPage
    cache: DocPagesSetName200ResponseMetaCacheDeltaPagesItemCache

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
