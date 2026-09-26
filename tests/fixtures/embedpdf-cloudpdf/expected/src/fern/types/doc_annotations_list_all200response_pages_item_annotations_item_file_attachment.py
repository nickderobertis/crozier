

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_file_attachment_blend_mode import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentBlendMode,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_file_attachment_color import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentColor,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_file_attachment_file import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentFile,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_file_attachment_flags import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentFlags,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_file_attachment_icon import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentIcon,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_file_attachment_identity_quality import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentIdentityQuality,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_file_attachment_in_reply_to import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentInReplyTo,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_file_attachment_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_file_attachment_rect import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentRect,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_file_attachment_ref import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentRef,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_file_attachment_reply_type import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentReplyType,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachment(UniversalBaseModel):
    ref: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentRef
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentFlags
    rect: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentReplyType],
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
    color: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentColor
    opacity: float
    icon: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentIcon
    file: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFileAttachmentFile

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
