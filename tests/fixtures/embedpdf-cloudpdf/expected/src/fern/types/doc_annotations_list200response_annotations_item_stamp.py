

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_stamp_blend_mode import (
    DocAnnotationsList200ResponseAnnotationsItemStampBlendMode,
)
from .doc_annotations_list200response_annotations_item_stamp_flags import (
    DocAnnotationsList200ResponseAnnotationsItemStampFlags,
)
from .doc_annotations_list200response_annotations_item_stamp_identity_quality import (
    DocAnnotationsList200ResponseAnnotationsItemStampIdentityQuality,
)
from .doc_annotations_list200response_annotations_item_stamp_in_reply_to import (
    DocAnnotationsList200ResponseAnnotationsItemStampInReplyTo,
)
from .doc_annotations_list200response_annotations_item_stamp_page import (
    DocAnnotationsList200ResponseAnnotationsItemStampPage,
)
from .doc_annotations_list200response_annotations_item_stamp_rect import (
    DocAnnotationsList200ResponseAnnotationsItemStampRect,
)
from .doc_annotations_list200response_annotations_item_stamp_ref import (
    DocAnnotationsList200ResponseAnnotationsItemStampRef,
)
from .doc_annotations_list200response_annotations_item_stamp_reply_type import (
    DocAnnotationsList200ResponseAnnotationsItemStampReplyType,
)
from .doc_annotations_list200response_annotations_item_stamp_unrotated_rect import (
    DocAnnotationsList200ResponseAnnotationsItemStampUnrotatedRect,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsList200ResponseAnnotationsItemStamp(UniversalBaseModel):
    ref: DocAnnotationsList200ResponseAnnotationsItemStampRef
    page: DocAnnotationsList200ResponseAnnotationsItemStampPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemStampIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsList200ResponseAnnotationsItemStampFlags
    rect: DocAnnotationsList200ResponseAnnotationsItemStampRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemStampBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemStampInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemStampReplyType],
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
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemStampUnrotatedRect],
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
