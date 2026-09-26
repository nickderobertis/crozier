

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_free_text_rich_text_body_align import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextBodyAlign,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_free_text_rich_text_body_decoration_item import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextBodyDecorationItem,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_free_text_rich_text_body_dir import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextBodyDir,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_free_text_rich_text_body_margins import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextBodyMargins,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_free_text_rich_text_body_script import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextBodyScript,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextBody(UniversalBaseModel):
    family: str
    weight: int
    italic: bool
    size: float
    color: str
    decoration: typing.List[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextBodyDecorationItem]
    script: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextBodyScript
    letter_spacing: typing_extensions.Annotated[
        float, FieldMetadata(alias="letterSpacing"), pydantic.Field(alias="letterSpacing")
    ]
    horizontal_scale: typing_extensions.Annotated[
        float, FieldMetadata(alias="horizontalScale"), pydantic.Field(alias="horizontalScale")
    ]
    unknown: typing.Optional[str] = None
    align: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextBodyAlign
    dir: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextBodyDir
    line_height: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="lineHeight"), pydantic.Field(alias="lineHeight")
    ] = None
    margins: typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichTextBodyMargins] = None
    text_indent: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="textIndent"), pydantic.Field(alias="textIndent")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
