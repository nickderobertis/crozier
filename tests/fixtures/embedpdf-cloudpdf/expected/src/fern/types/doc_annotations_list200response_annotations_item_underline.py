

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_underline_blend_mode import (
    DocAnnotationsList200ResponseAnnotationsItemUnderlineBlendMode,
)
from .doc_annotations_list200response_annotations_item_underline_color import (
    DocAnnotationsList200ResponseAnnotationsItemUnderlineColor,
)
from .doc_annotations_list200response_annotations_item_underline_flags import (
    DocAnnotationsList200ResponseAnnotationsItemUnderlineFlags,
)
from .doc_annotations_list200response_annotations_item_underline_identity_quality import (
    DocAnnotationsList200ResponseAnnotationsItemUnderlineIdentityQuality,
)
from .doc_annotations_list200response_annotations_item_underline_in_reply_to import (
    DocAnnotationsList200ResponseAnnotationsItemUnderlineInReplyTo,
)
from .doc_annotations_list200response_annotations_item_underline_page import (
    DocAnnotationsList200ResponseAnnotationsItemUnderlinePage,
)
from .doc_annotations_list200response_annotations_item_underline_quad_points_item import (
    DocAnnotationsList200ResponseAnnotationsItemUnderlineQuadPointsItem,
)
from .doc_annotations_list200response_annotations_item_underline_rect import (
    DocAnnotationsList200ResponseAnnotationsItemUnderlineRect,
)
from .doc_annotations_list200response_annotations_item_underline_ref import (
    DocAnnotationsList200ResponseAnnotationsItemUnderlineRef,
)
from .doc_annotations_list200response_annotations_item_underline_reply_type import (
    DocAnnotationsList200ResponseAnnotationsItemUnderlineReplyType,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsList200ResponseAnnotationsItemUnderline(UniversalBaseModel):
    ref: DocAnnotationsList200ResponseAnnotationsItemUnderlineRef
    page: DocAnnotationsList200ResponseAnnotationsItemUnderlinePage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemUnderlineIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsList200ResponseAnnotationsItemUnderlineFlags
    rect: DocAnnotationsList200ResponseAnnotationsItemUnderlineRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemUnderlineBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemUnderlineInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemUnderlineReplyType],
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
    color: DocAnnotationsList200ResponseAnnotationsItemUnderlineColor
    opacity: float
    quad_points: typing_extensions.Annotated[
        typing.List[DocAnnotationsList200ResponseAnnotationsItemUnderlineQuadPointsItem],
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
