

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_free_text_rich_text_paragraphs_item_align import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextParagraphsItemAlign,
)
from .doc_annotations_list200response_annotations_item_free_text_rich_text_paragraphs_item_dir import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextParagraphsItemDir,
)
from .doc_annotations_list200response_annotations_item_free_text_rich_text_paragraphs_item_margins import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextParagraphsItemMargins,
)
from .doc_annotations_list200response_annotations_item_free_text_rich_text_paragraphs_item_runs_item import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextParagraphsItemRunsItem,
)


class DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextParagraphsItem(UniversalBaseModel):
    align: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextParagraphsItemAlign] = None
    dir: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextParagraphsItemDir] = None
    line_height: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="lineHeight"), pydantic.Field(alias="lineHeight")
    ] = None
    margins: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextParagraphsItemMargins] = None
    text_indent: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="textIndent"), pydantic.Field(alias="textIndent")
    ] = None
    unknown: typing.Optional[str] = None
    runs: typing.List[DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextParagraphsItemRunsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
