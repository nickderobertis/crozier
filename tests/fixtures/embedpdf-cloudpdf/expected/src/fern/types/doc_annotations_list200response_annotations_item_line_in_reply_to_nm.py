

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list200response_annotations_item_line_in_reply_to_nm_page import (
    DocAnnotationsList200ResponseAnnotationsItemLineInReplyToNmPage,
)


class DocAnnotationsList200ResponseAnnotationsItemLineInReplyToNm(UniversalBaseModel):
    page: DocAnnotationsList200ResponseAnnotationsItemLineInReplyToNmPage
    nm: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
