

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list_all200response_pages_item_annotations_item_redact_ref_index_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactRefIndexPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_redact_ref_index_revision import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactRefIndexRevision,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactRefIndex(UniversalBaseModel):
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactRefIndexPage
    index: int
    revision: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
