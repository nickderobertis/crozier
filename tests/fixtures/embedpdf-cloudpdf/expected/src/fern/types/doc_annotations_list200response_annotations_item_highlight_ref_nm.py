

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list200response_annotations_item_highlight_ref_nm_page import (
    DocAnnotationsList200ResponseAnnotationsItemHighlightRefNmPage,
)


class DocAnnotationsList200ResponseAnnotationsItemHighlightRefNm(UniversalBaseModel):
    page: DocAnnotationsList200ResponseAnnotationsItemHighlightRefNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
