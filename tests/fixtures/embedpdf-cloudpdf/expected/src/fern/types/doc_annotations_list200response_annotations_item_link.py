

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_link_blend_mode import (
    DocAnnotationsList200ResponseAnnotationsItemLinkBlendMode,
)
from .doc_annotations_list200response_annotations_item_link_flags import (
    DocAnnotationsList200ResponseAnnotationsItemLinkFlags,
)
from .doc_annotations_list200response_annotations_item_link_identity_quality import (
    DocAnnotationsList200ResponseAnnotationsItemLinkIdentityQuality,
)
from .doc_annotations_list200response_annotations_item_link_in_reply_to import (
    DocAnnotationsList200ResponseAnnotationsItemLinkInReplyTo,
)
from .doc_annotations_list200response_annotations_item_link_page import (
    DocAnnotationsList200ResponseAnnotationsItemLinkPage,
)
from .doc_annotations_list200response_annotations_item_link_rect import (
    DocAnnotationsList200ResponseAnnotationsItemLinkRect,
)
from .doc_annotations_list200response_annotations_item_link_ref import (
    DocAnnotationsList200ResponseAnnotationsItemLinkRef,
)
from .doc_annotations_list200response_annotations_item_link_reply_type import (
    DocAnnotationsList200ResponseAnnotationsItemLinkReplyType,
)
from .doc_annotations_list200response_annotations_item_link_target import (
    DocAnnotationsList200ResponseAnnotationsItemLinkTarget,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsList200ResponseAnnotationsItemLink(UniversalBaseModel):
    ref: DocAnnotationsList200ResponseAnnotationsItemLinkRef
    page: DocAnnotationsList200ResponseAnnotationsItemLinkPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemLinkIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsList200ResponseAnnotationsItemLinkFlags
    rect: DocAnnotationsList200ResponseAnnotationsItemLinkRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemLinkBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemLinkInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemLinkReplyType],
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
    target: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemLinkTarget] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
