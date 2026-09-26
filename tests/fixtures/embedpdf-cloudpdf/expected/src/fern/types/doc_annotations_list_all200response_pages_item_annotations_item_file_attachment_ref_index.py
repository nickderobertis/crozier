

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list_all200response_pages_item_annotations_item_file_attachment_ref_index_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentRefIndexPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_file_attachment_ref_index_revision import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentRefIndexRevision,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentRefIndex(UniversalBaseModel):
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentRefIndexPage
    index: int
    revision: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
