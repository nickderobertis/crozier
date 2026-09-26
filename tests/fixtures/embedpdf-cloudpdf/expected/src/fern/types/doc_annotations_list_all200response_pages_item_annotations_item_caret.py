

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_caret_blend_mode import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretBlendMode,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_caret_color import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretColor,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_caret_flags import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretFlags,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_caret_identity_quality import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretIdentityQuality,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_caret_in_reply_to import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretInReplyTo,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_caret_intent import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretIntent,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_caret_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_caret_rect import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretRect,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_caret_rect_differences import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretRectDifferences,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_caret_ref import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretRef,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_caret_reply_type import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretReplyType,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_caret_unrotated_rect import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretUnrotatedRect,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaret(UniversalBaseModel):
    ref: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretRef
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretFlags
    rect: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretReplyType],
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
    color: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretColor
    opacity: float
    intent: typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretIntent] = None
    rect_differences: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretRectDifferences],
        FieldMetadata(alias="rectDifferences"),
        pydantic.Field(alias="rectDifferences"),
    ] = None
    rotation: typing.Optional[float] = None
    unrotated_rect: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCaretUnrotatedRect],
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
