

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list_all200response_pages_item_annotations_item_free_text_rich_text_body import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextBody,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_free_text_rich_text_paragraphs_item import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextParagraphsItem,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichText(UniversalBaseModel):
    body: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextBody
    paragraphs: typing.List[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextParagraphsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
