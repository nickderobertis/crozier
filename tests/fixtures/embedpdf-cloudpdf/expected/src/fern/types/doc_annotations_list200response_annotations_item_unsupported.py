

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_unsupported_blend_mode import (
    DocAnnotationsList200ResponseAnnotationsItemUnsupportedBlendMode,
)
from .doc_annotations_list200response_annotations_item_unsupported_flags import (
    DocAnnotationsList200ResponseAnnotationsItemUnsupportedFlags,
)
from .doc_annotations_list200response_annotations_item_unsupported_identity_quality import (
    DocAnnotationsList200ResponseAnnotationsItemUnsupportedIdentityQuality,
)
from .doc_annotations_list200response_annotations_item_unsupported_in_reply_to import (
    DocAnnotationsList200ResponseAnnotationsItemUnsupportedInReplyTo,
)
from .doc_annotations_list200response_annotations_item_unsupported_page import (
    DocAnnotationsList200ResponseAnnotationsItemUnsupportedPage,
)
from .doc_annotations_list200response_annotations_item_unsupported_rect import (
    DocAnnotationsList200ResponseAnnotationsItemUnsupportedRect,
)
from .doc_annotations_list200response_annotations_item_unsupported_ref import (
    DocAnnotationsList200ResponseAnnotationsItemUnsupportedRef,
)
from .doc_annotations_list200response_annotations_item_unsupported_reply_type import (
    DocAnnotationsList200ResponseAnnotationsItemUnsupportedReplyType,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsList200ResponseAnnotationsItemUnsupported(UniversalBaseModel):
    ref: DocAnnotationsList200ResponseAnnotationsItemUnsupportedRef
    page: DocAnnotationsList200ResponseAnnotationsItemUnsupportedPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemUnsupportedIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsList200ResponseAnnotationsItemUnsupportedFlags
    rect: DocAnnotationsList200ResponseAnnotationsItemUnsupportedRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemUnsupportedBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemUnsupportedInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemUnsupportedReplyType],
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
    raw_subtype_code: typing_extensions.Annotated[
        int, FieldMetadata(alias="rawSubtypeCode"), pydantic.Field(alias="rawSubtypeCode")
    ]
    raw_subtype_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="rawSubtypeName"), pydantic.Field(alias="rawSubtypeName")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
