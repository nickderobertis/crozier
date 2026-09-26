

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_free_text_rich_text_paragraphs_item_align import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextParagraphsItemAlign,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_free_text_rich_text_paragraphs_item_dir import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextParagraphsItemDir,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_free_text_rich_text_paragraphs_item_margins import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextParagraphsItemMargins,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_free_text_rich_text_paragraphs_item_runs_item import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextParagraphsItemRunsItem,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextParagraphsItem(UniversalBaseModel):
    align: typing.Optional[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextParagraphsItemAlign
    ] = None
    dir: typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextParagraphsItemDir] = (
        None
    )
    line_height: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="lineHeight"), pydantic.Field(alias="lineHeight")
    ] = None
    margins: typing.Optional[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextParagraphsItemMargins
    ] = None
    text_indent: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="textIndent"), pydantic.Field(alias="textIndent")
    ] = None
    unknown: typing.Optional[str] = None
    runs: typing.List[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextParagraphsItemRunsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
