

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_file_attachment_blend_mode import (
    DocAnnotationsList200ResponseAnnotationsItemFileAttachmentBlendMode,
)
from .doc_annotations_list200response_annotations_item_file_attachment_color import (
    DocAnnotationsList200ResponseAnnotationsItemFileAttachmentColor,
)
from .doc_annotations_list200response_annotations_item_file_attachment_file import (
    DocAnnotationsList200ResponseAnnotationsItemFileAttachmentFile,
)
from .doc_annotations_list200response_annotations_item_file_attachment_flags import (
    DocAnnotationsList200ResponseAnnotationsItemFileAttachmentFlags,
)
from .doc_annotations_list200response_annotations_item_file_attachment_icon import (
    DocAnnotationsList200ResponseAnnotationsItemFileAttachmentIcon,
)
from .doc_annotations_list200response_annotations_item_file_attachment_identity_quality import (
    DocAnnotationsList200ResponseAnnotationsItemFileAttachmentIdentityQuality,
)
from .doc_annotations_list200response_annotations_item_file_attachment_in_reply_to import (
    DocAnnotationsList200ResponseAnnotationsItemFileAttachmentInReplyTo,
)
from .doc_annotations_list200response_annotations_item_file_attachment_page import (
    DocAnnotationsList200ResponseAnnotationsItemFileAttachmentPage,
)
from .doc_annotations_list200response_annotations_item_file_attachment_rect import (
    DocAnnotationsList200ResponseAnnotationsItemFileAttachmentRect,
)
from .doc_annotations_list200response_annotations_item_file_attachment_ref import (
    DocAnnotationsList200ResponseAnnotationsItemFileAttachmentRef,
)
from .doc_annotations_list200response_annotations_item_file_attachment_reply_type import (
    DocAnnotationsList200ResponseAnnotationsItemFileAttachmentReplyType,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsList200ResponseAnnotationsItemFileAttachment(UniversalBaseModel):
    ref: DocAnnotationsList200ResponseAnnotationsItemFileAttachmentRef
    page: DocAnnotationsList200ResponseAnnotationsItemFileAttachmentPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemFileAttachmentIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsList200ResponseAnnotationsItemFileAttachmentFlags
    rect: DocAnnotationsList200ResponseAnnotationsItemFileAttachmentRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemFileAttachmentBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemFileAttachmentInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemFileAttachmentReplyType],
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
    color: DocAnnotationsList200ResponseAnnotationsItemFileAttachmentColor
    opacity: float
    icon: DocAnnotationsList200ResponseAnnotationsItemFileAttachmentIcon
    file: DocAnnotationsList200ResponseAnnotationsItemFileAttachmentFile

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
