

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_free_text_rich_text_paragraphs_item_runs_item_style_decoration_item import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextParagraphsItemRunsItemStyleDecorationItem,
)
from .doc_annotations_list200response_annotations_item_free_text_rich_text_paragraphs_item_runs_item_style_script import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextParagraphsItemRunsItemStyleScript,
)


class DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextParagraphsItemRunsItemStyle(UniversalBaseModel):
    family: typing.Optional[str] = None
    weight: typing.Optional[int] = None
    italic: typing.Optional[bool] = None
    size: typing.Optional[float] = None
    color: typing.Optional[str] = None
    decoration: typing.Optional[
        typing.List[
            DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextParagraphsItemRunsItemStyleDecorationItem
        ]
    ] = None
    script: typing.Optional[
        DocAnnotationsList200ResponseAnnotationsItemFreeTextRichTextParagraphsItemRunsItemStyleScript
    ] = None
    letter_spacing: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="letterSpacing"), pydantic.Field(alias="letterSpacing")
    ] = None
    horizontal_scale: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="horizontalScale"), pydantic.Field(alias="horizontalScale")
    ] = None
    unknown: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
