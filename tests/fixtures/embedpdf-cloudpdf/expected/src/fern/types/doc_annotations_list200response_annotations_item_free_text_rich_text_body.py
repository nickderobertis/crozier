

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_free_text_rich_text_body_align import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextBodyAlign,
)
from .doc_annotations_list200response_annotations_item_free_text_rich_text_body_decoration_item import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextBodyDecorationItem,
)
from .doc_annotations_list200response_annotations_item_free_text_rich_text_body_dir import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextBodyDir,
)
from .doc_annotations_list200response_annotations_item_free_text_rich_text_body_margins import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextBodyMargins,
)
from .doc_annotations_list200response_annotations_item_free_text_rich_text_body_script import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextBodyScript,
)


class DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextBody(UniversalBaseModel):
    family: str
    weight: int
    italic: bool
    size: float
    color: str
    decoration: typing.List[DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextBodyDecorationItem]
    script: DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextBodyScript
    letter_spacing: typing_extensions.Annotated[
        float, FieldMetadata(alias="letterSpacing"), pydantic.Field(alias="letterSpacing")
    ]
    horizontal_scale: typing_extensions.Annotated[
        float, FieldMetadata(alias="horizontalScale"), pydantic.Field(alias="horizontalScale")
    ]
    unknown: typing.Optional[str] = None
    align: DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextBodyAlign
    dir: DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextBodyDir
    line_height: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="lineHeight"), pydantic.Field(alias="lineHeight")
    ] = None
    margins: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextBodyMargins] = None
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
