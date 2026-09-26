

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_highlight_blend_mode import (
    DocAnnotationsList200ResponseAnnotationsItemHighlightBlendMode,
)
from .doc_annotations_list200response_annotations_item_highlight_color import (
    DocAnnotationsList200ResponseAnnotationsItemHighlightColor,
)
from .doc_annotations_list200response_annotations_item_highlight_flags import (
    DocAnnotationsList200ResponseAnnotationsItemHighlightFlags,
)
from .doc_annotations_list200response_annotations_item_highlight_identity_quality import (
    DocAnnotationsList200ResponseAnnotationsItemHighlightIdentityQuality,
)
from .doc_annotations_list200response_annotations_item_highlight_in_reply_to import (
    DocAnnotationsList200ResponseAnnotationsItemHighlightInReplyTo,
)
from .doc_annotations_list200response_annotations_item_highlight_page import (
    DocAnnotationsList200ResponseAnnotationsItemHighlightPage,
)
from .doc_annotations_list200response_annotations_item_highlight_quad_points_item import (
    DocAnnotationsList200ResponseAnnotationsItemHighlightQuadPointsItem,
)
from .doc_annotations_list200response_annotations_item_highlight_rect import (
    DocAnnotationsList200ResponseAnnotationsItemHighlightRect,
)
from .doc_annotations_list200response_annotations_item_highlight_ref import (
    DocAnnotationsList200ResponseAnnotationsItemHighlightRef,
)
from .doc_annotations_list200response_annotations_item_highlight_reply_type import (
    DocAnnotationsList200ResponseAnnotationsItemHighlightReplyType,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsList200ResponseAnnotationsItemHighlight(UniversalBaseModel):
    ref: DocAnnotationsList200ResponseAnnotationsItemHighlightRef
    page: DocAnnotationsList200ResponseAnnotationsItemHighlightPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemHighlightIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsList200ResponseAnnotationsItemHighlightFlags
    rect: DocAnnotationsList200ResponseAnnotationsItemHighlightRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemHighlightBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemHighlightInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemHighlightReplyType],
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
    color: DocAnnotationsList200ResponseAnnotationsItemHighlightColor
    opacity: float
    quad_points: typing_extensions.Annotated[
        typing.List[DocAnnotationsList200ResponseAnnotationsItemHighlightQuadPointsItem],
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
