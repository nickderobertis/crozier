

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list200response_annotations_item_redact_ref_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemRedactRefIndexPage,
)
from .doc_annotations_list200response_annotations_item_redact_ref_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemRedactRefIndexRevision,
)


class DocAnnotationsList200ResponseAnnotationsItemRedactRefIndex(UniversalBaseModel):
    page: DocAnnotationsList200ResponseAnnotationsItemRedactRefIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemRedactRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
