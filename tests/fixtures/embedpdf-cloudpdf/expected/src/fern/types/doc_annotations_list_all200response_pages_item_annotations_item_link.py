

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_link_blend_mode import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkBlendMode,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_link_flags import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkFlags,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_link_identity_quality import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkIdentityQuality,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_link_in_reply_to import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkInReplyTo,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_link_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_link_rect import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkRect,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_link_ref import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkRef,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_link_reply_type import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkReplyType,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_link_target import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkTarget,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLink(UniversalBaseModel):
    ref: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkRef
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkFlags
    rect: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkReplyType],
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
    target: typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkTarget] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
