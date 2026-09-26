

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_unsupported_blend_mode import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedBlendMode,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_unsupported_flags import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedFlags,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_unsupported_identity_quality import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedIdentityQuality,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_unsupported_in_reply_to import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedInReplyTo,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_unsupported_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_unsupported_rect import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedRect,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_unsupported_ref import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedRef,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_unsupported_reply_type import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedReplyType,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupported(UniversalBaseModel):
    ref: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedRef
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedFlags
    rect: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedReplyType],
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
