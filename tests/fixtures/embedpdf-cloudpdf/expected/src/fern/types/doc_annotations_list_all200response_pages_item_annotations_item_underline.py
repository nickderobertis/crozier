

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_underline_blend_mode import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineBlendMode,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_underline_color import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineColor,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_underline_flags import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineFlags,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_underline_identity_quality import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineIdentityQuality,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_underline_in_reply_to import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineInReplyTo,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_underline_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlinePage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_underline_quad_points_item import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineQuadPointsItem,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_underline_rect import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineRect,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_underline_ref import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineRef,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_underline_reply_type import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineReplyType,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderline(UniversalBaseModel):
    ref: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineRef
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlinePage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineFlags
    rect: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineReplyType],
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
    color: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineColor
    opacity: float
    quad_points: typing_extensions.Annotated[
        typing.List[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineQuadPointsItem],
        FieldMetadata(alias="quadPoints"),
        pydantic.Field(alias="quadPoints"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
