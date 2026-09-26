

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_free_text_blend_mode import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextBlendMode,
)
from .doc_annotations_list200response_annotations_item_free_text_border_style import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextBorderStyle,
)
from .doc_annotations_list200response_annotations_item_free_text_color import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextColor,
)
from .doc_annotations_list200response_annotations_item_free_text_flags import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextFlags,
)
from .doc_annotations_list200response_annotations_item_free_text_font_color import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextFontColor,
)
from .doc_annotations_list200response_annotations_item_free_text_identity_quality import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextIdentityQuality,
)
from .doc_annotations_list200response_annotations_item_free_text_in_reply_to import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextInReplyTo,
)
from .doc_annotations_list200response_annotations_item_free_text_intent import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextIntent,
)
from .doc_annotations_list200response_annotations_item_free_text_interior_color import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextInteriorColor,
)
from .doc_annotations_list200response_annotations_item_free_text_line_ending import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextLineEnding,
)
from .doc_annotations_list200response_annotations_item_free_text_page import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextPage,
)
from .doc_annotations_list200response_annotations_item_free_text_rect import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextRect,
)
from .doc_annotations_list200response_annotations_item_free_text_rect_differences import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextRectDifferences,
)
from .doc_annotations_list200response_annotations_item_free_text_ref import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextRef,
)
from .doc_annotations_list200response_annotations_item_free_text_reply_type import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextReplyType,
)
from .doc_annotations_list200response_annotations_item_free_text_rich_text import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextRichText,
)
from .doc_annotations_list200response_annotations_item_free_text_text_align import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextTextAlign,
)
from .doc_annotations_list200response_annotations_item_free_text_unrotated_rect import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextUnrotatedRect,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsList200ResponseAnnotationsItemFreeText(UniversalBaseModel):
    ref: DocAnnotationsList200ResponseAnnotationsItemFreeTextRef
    page: DocAnnotationsList200ResponseAnnotationsItemFreeTextPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemFreeTextIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsList200ResponseAnnotationsItemFreeTextFlags
    rect: DocAnnotationsList200ResponseAnnotationsItemFreeTextRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemFreeTextBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemFreeTextInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemFreeTextReplyType],
        FieldMetadata(alias="replyType"),
        pydantic.Field(alias="replyType"),
    ] = None
    user_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="userId"), pydantic.Field(alias="userId")
    ] = None
    group_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="groupId"), pydantic.Field(alias="groupId")
    ] = None
    created_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")
    ] = None
    updated_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="updatedBy"), pydantic.Field(alias="updatedBy")
    ] = None
    actions: typing.Optional[PdfAnnotationActions] = None
    intent: DocAnnotationsList200ResponseAnnotationsItemFreeTextIntent
    font_family: typing_extensions.Annotated[str, FieldMetadata(alias="fontFamily"), pydantic.Field(alias="fontFamily")]
    font_size: typing_extensions.Annotated[float, FieldMetadata(alias="fontSize"), pydantic.Field(alias="fontSize")]
    text_align: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemFreeTextTextAlign,
        FieldMetadata(alias="textAlign"),
        pydantic.Field(alias="textAlign"),
    ]
    rich_text: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemFreeTextRichText,
        FieldMetadata(alias="richText"),
        pydantic.Field(alias="richText"),
    ]
    color: DocAnnotationsList200ResponseAnnotationsItemFreeTextColor
    font_color: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemFreeTextFontColor],
        FieldMetadata(alias="fontColor"),
        pydantic.Field(alias="fontColor"),
    ] = None
    interior_color: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemFreeTextInteriorColor],
        FieldMetadata(alias="interiorColor"),
        pydantic.Field(alias="interiorColor"),
    ] = None
    opacity: float
    stroke_width: typing_extensions.Annotated[
        float, FieldMetadata(alias="strokeWidth"), pydantic.Field(alias="strokeWidth")
    ]
    border_style: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemFreeTextBorderStyle,
        FieldMetadata(alias="borderStyle"),
        pydantic.Field(alias="borderStyle"),
    ]
    dash_array: typing_extensions.Annotated[
        typing.Optional[typing.List[float]], FieldMetadata(alias="dashArray"), pydantic.Field(alias="dashArray")
    ] = None
    rect_differences: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemFreeTextRectDifferences],
        FieldMetadata(alias="rectDifferences"),
        pydantic.Field(alias="rectDifferences"),
    ] = None
    callout_line: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Any]],
        FieldMetadata(alias="calloutLine"),
        pydantic.Field(alias="calloutLine"),
    ] = None
    line_ending: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemFreeTextLineEnding],
        FieldMetadata(alias="lineEnding"),
        pydantic.Field(alias="lineEnding"),
    ] = None
    rotation: typing.Optional[float] = None
    unrotated_rect: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemFreeTextUnrotatedRect],
        FieldMetadata(alias="unrotatedRect"),
        pydantic.Field(alias="unrotatedRect"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
