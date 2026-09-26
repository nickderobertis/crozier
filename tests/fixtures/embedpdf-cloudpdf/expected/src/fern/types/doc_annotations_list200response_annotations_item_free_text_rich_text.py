

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list200response_annotations_item_free_text_rich_text_body import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextBody,
)
from .doc_annotations_list200response_annotations_item_free_text_rich_text_paragraphs_item import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextParagraphsItem,
)


class DocAnnotationsList200ResponseAnnotationsItemFreeTextRichText(UniversalBaseModel):
    body: DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextBody
    paragraphs: typing.List[DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextParagraphsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
