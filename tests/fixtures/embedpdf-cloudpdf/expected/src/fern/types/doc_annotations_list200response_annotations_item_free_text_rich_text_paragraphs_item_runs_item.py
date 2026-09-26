

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list200response_annotations_item_free_text_rich_text_paragraphs_item_runs_item_style import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextParagraphsItemRunsItemStyle,
)


class DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextParagraphsItemRunsItem(UniversalBaseModel):
    text: str
    style: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextParagraphsItemRunsItemStyle] = (
        None
    )

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
