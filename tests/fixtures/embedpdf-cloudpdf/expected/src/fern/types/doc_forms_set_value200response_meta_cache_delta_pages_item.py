

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_forms_set_value200response_meta_cache_delta_pages_item_cache import (
    DocFormsSetValue200ResponseMetaCacheDeltaPagesItemCache,
)
from .doc_forms_set_value200response_meta_cache_delta_pages_item_page import (
    DocFormsSetValue200ResponseMetaCacheDeltaPagesItemPage,
)


class DocFormsSetValue200ResponseMetaCacheDeltaPagesItem(UniversalBaseModel):
    page: DocFormsSetValue200ResponseMetaCacheDeltaPagesItemPage
    cache: DocFormsSetValue200ResponseMetaCacheDeltaPagesItemCache

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
