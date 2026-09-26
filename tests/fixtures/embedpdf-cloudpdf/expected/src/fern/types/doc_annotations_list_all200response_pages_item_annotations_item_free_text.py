

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_free_text_blend_mode import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextBlendMode,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_free_text_border_style import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextBorderStyle,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_free_text_color import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextColor,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_free_text_flags import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextFlags,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_free_text_font_color import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextFontColor,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_free_text_identity_quality import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextIdentityQuality,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_free_text_in_reply_to import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextInReplyTo,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_free_text_intent import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextIntent,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_free_text_interior_color import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextInteriorColor,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_free_text_line_ending import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextLineEnding,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_free_text_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_free_text_rect import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRect,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_free_text_rect_differences import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRectDifferences,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_free_text_ref import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRef,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_free_text_reply_type import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextReplyType,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_free_text_rich_text import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichText,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_free_text_text_align import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextTextAlign,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_free_text_unrotated_rect import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextUnrotatedRect,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeText(UniversalBaseModel):
    ref: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRef
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextFlags
    rect: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextReplyType],
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
    intent: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextIntent
    font_family: typing_extensions.Annotated[str, FieldMetadata(alias="fontFamily"), pydantic.Field(alias="fontFamily")]
    font_size: typing_extensions.Annotated[float, FieldMetadata(alias="fontSize"), pydantic.Field(alias="fontSize")]
    text_align: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextTextAlign,
        FieldMetadata(alias="textAlign"),
        pydantic.Field(alias="textAlign"),
    ]
    rich_text: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRichText,
        FieldMetadata(alias="richText"),
        pydantic.Field(alias="richText"),
    ]
    color: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextColor
    font_color: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextFontColor],
        FieldMetadata(alias="fontColor"),
        pydantic.Field(alias="fontColor"),
    ] = None
    interior_color: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextInteriorColor],
        FieldMetadata(alias="interiorColor"),
        pydantic.Field(alias="interiorColor"),
    ] = None
    opacity: float
    stroke_width: typing_extensions.Annotated[
        float, FieldMetadata(alias="strokeWidth"), pydantic.Field(alias="strokeWidth")
    ]
    border_style: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextBorderStyle,
        FieldMetadata(alias="borderStyle"),
        pydantic.Field(alias="borderStyle"),
    ]
    dash_array: typing_extensions.Annotated[
        typing.Optional[typing.List[float]], FieldMetadata(alias="dashArray"), pydantic.Field(alias="dashArray")
    ] = None
    rect_differences: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRectDifferences],
        FieldMetadata(alias="rectDifferences"),
        pydantic.Field(alias="rectDifferences"),
    ] = None
    callout_line: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Any]],
        FieldMetadata(alias="calloutLine"),
        pydantic.Field(alias="calloutLine"),
    ] = None
    line_ending: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextLineEnding],
        FieldMetadata(alias="lineEnding"),
        pydantic.Field(alias="lineEnding"),
    ] = None
    rotation: typing.Optional[float] = None
    unrotated_rect: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextUnrotatedRect],
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
