

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_caret_blend_mode import (
    DocAnnotationsList200ResponseAnnotationsItemCaretBlendMode,
)
from .doc_annotations_list200response_annotations_item_caret_color import (
    DocAnnotationsList200ResponseAnnotationsItemCaretColor,
)
from .doc_annotations_list200response_annotations_item_caret_flags import (
    DocAnnotationsList200ResponseAnnotationsItemCaretFlags,
)
from .doc_annotations_list200response_annotations_item_caret_identity_quality import (
    DocAnnotationsList200ResponseAnnotationsItemCaretIdentityQuality,
)
from .doc_annotations_list200response_annotations_item_caret_in_reply_to import (
    DocAnnotationsList200ResponseAnnotationsItemCaretInReplyTo,
)
from .doc_annotations_list200response_annotations_item_caret_intent import (
    DocAnnotationsList200ResponseAnnotationsItemCaretIntent,
)
from .doc_annotations_list200response_annotations_item_caret_page import (
    DocAnnotationsList200ResponseAnnotationsItemCaretPage,
)
from .doc_annotations_list200response_annotations_item_caret_rect import (
    DocAnnotationsList200ResponseAnnotationsItemCaretRect,
)
from .doc_annotations_list200response_annotations_item_caret_rect_differences import (
    DocAnnotationsList200ResponseAnnotationsItemCaretRectDifferences,
)
from .doc_annotations_list200response_annotations_item_caret_ref import (
    DocAnnotationsList200ResponseAnnotationsItemCaretRef,
)
from .doc_annotations_list200response_annotations_item_caret_reply_type import (
    DocAnnotationsList200ResponseAnnotationsItemCaretReplyType,
)
from .doc_annotations_list200response_annotations_item_caret_unrotated_rect import (
    DocAnnotationsList200ResponseAnnotationsItemCaretUnrotatedRect,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsList200ResponseAnnotationsItemCaret(UniversalBaseModel):
    ref: DocAnnotationsList200ResponseAnnotationsItemCaretRef
    page: DocAnnotationsList200ResponseAnnotationsItemCaretPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemCaretIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsList200ResponseAnnotationsItemCaretFlags
    rect: DocAnnotationsList200ResponseAnnotationsItemCaretRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemCaretBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemCaretInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemCaretReplyType],
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
    color: DocAnnotationsList200ResponseAnnotationsItemCaretColor
    opacity: float
    intent: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemCaretIntent] = None
    rect_differences: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemCaretRectDifferences],
        FieldMetadata(alias="rectDifferences"),
        pydantic.Field(alias="rectDifferences"),
    ] = None
    rotation: typing.Optional[float] = None
    unrotated_rect: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemCaretUnrotatedRect],
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
