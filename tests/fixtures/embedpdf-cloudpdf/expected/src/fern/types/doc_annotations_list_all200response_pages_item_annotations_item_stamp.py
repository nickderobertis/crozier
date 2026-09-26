

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_stamp_blend_mode import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampBlendMode,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_stamp_flags import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampFlags,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_stamp_identity_quality import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampIdentityQuality,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_stamp_in_reply_to import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampInReplyTo,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_stamp_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_stamp_rect import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampRect,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_stamp_ref import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampRef,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_stamp_reply_type import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampReplyType,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_stamp_unrotated_rect import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampUnrotatedRect,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStamp(UniversalBaseModel):
    ref: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampRef
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampFlags
    rect: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampReplyType],
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
    name: typing.Optional[str] = None
    rotation: typing.Optional[float] = None
    unrotated_rect: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampUnrotatedRect],
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
