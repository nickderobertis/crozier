

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_forms_import_data200response_meta_cache_delta_pages_item_cache import (
    DocFormsImportData200ResponseMetaCacheDeltaPagesItemCache,
)
from .doc_forms_import_data200response_meta_cache_delta_pages_item_page import (
    DocFormsImportData200ResponseMetaCacheDeltaPagesItemPage,
)


class DocFormsImportData200ResponseMetaCacheDeltaPagesItem(UniversalBaseModel):
    page: DocFormsImportData200ResponseMetaCacheDeltaPagesItemPage
    cache: DocFormsImportData200ResponseMetaCacheDeltaPagesItemCache

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
