

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_line_blend_mode import (
    DocAnnotationsList200ResponseAnnotationsItemLineBlendMode,
)
from .doc_annotations_list200response_annotations_item_line_border_style import (
    DocAnnotationsList200ResponseAnnotationsItemLineBorderStyle,
)
from .doc_annotations_list200response_annotations_item_line_caption import (
    DocAnnotationsList200ResponseAnnotationsItemLineCaption,
)
from .doc_annotations_list200response_annotations_item_line_color import (
    DocAnnotationsList200ResponseAnnotationsItemLineColor,
)
from .doc_annotations_list200response_annotations_item_line_flags import (
    DocAnnotationsList200ResponseAnnotationsItemLineFlags,
)
from .doc_annotations_list200response_annotations_item_line_identity_quality import (
    DocAnnotationsList200ResponseAnnotationsItemLineIdentityQuality,
)
from .doc_annotations_list200response_annotations_item_line_in_reply_to import (
    DocAnnotationsList200ResponseAnnotationsItemLineInReplyTo,
)
from .doc_annotations_list200response_annotations_item_line_intent import (
    DocAnnotationsList200ResponseAnnotationsItemLineIntent,
)
from .doc_annotations_list200response_annotations_item_line_interior_color import (
    DocAnnotationsList200ResponseAnnotationsItemLineInteriorColor,
)
from .doc_annotations_list200response_annotations_item_line_leader import (
    DocAnnotationsList200ResponseAnnotationsItemLineLeader,
)
from .doc_annotations_list200response_annotations_item_line_line_endings import (
    DocAnnotationsList200ResponseAnnotationsItemLineLineEndings,
)
from .doc_annotations_list200response_annotations_item_line_line_points import (
    DocAnnotationsList200ResponseAnnotationsItemLineLinePoints,
)
from .doc_annotations_list200response_annotations_item_line_measure import (
    DocAnnotationsList200ResponseAnnotationsItemLineMeasure,
)
from .doc_annotations_list200response_annotations_item_line_page import (
    DocAnnotationsList200ResponseAnnotationsItemLinePage,
)
from .doc_annotations_list200response_annotations_item_line_rect import (
    DocAnnotationsList200ResponseAnnotationsItemLineRect,
)
from .doc_annotations_list200response_annotations_item_line_ref import (
    DocAnnotationsList200ResponseAnnotationsItemLineRef,
)
from .doc_annotations_list200response_annotations_item_line_reply_type import (
    DocAnnotationsList200ResponseAnnotationsItemLineReplyType,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsList200ResponseAnnotationsItemLine(UniversalBaseModel):
    intent: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemLineIntent] = None
    measure: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemLineMeasure] = None
    caption: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemLineCaption] = None
    leader: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemLineLeader] = None
    ref: DocAnnotationsList200ResponseAnnotationsItemLineRef
    page: DocAnnotationsList200ResponseAnnotationsItemLinePage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemLineIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsList200ResponseAnnotationsItemLineFlags
    rect: DocAnnotationsList200ResponseAnnotationsItemLineRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemLineBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemLineInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemLineReplyType],
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
    color: DocAnnotationsList200ResponseAnnotationsItemLineColor
    opacity: float
    stroke_width: typing_extensions.Annotated[
        float, FieldMetadata(alias="strokeWidth"), pydantic.Field(alias="strokeWidth")
    ]
    border_style: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemLineBorderStyle,
        FieldMetadata(alias="borderStyle"),
        pydantic.Field(alias="borderStyle"),
    ]
    dash_array: typing_extensions.Annotated[
        typing.Optional[typing.List[float]], FieldMetadata(alias="dashArray"), pydantic.Field(alias="dashArray")
    ] = None
    interior_color: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemLineInteriorColor],
        FieldMetadata(alias="interiorColor"),
        pydantic.Field(alias="interiorColor"),
    ] = None
    line_points: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemLineLinePoints,
        FieldMetadata(alias="linePoints"),
        pydantic.Field(alias="linePoints"),
    ]
    line_endings: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemLineLineEndings,
        FieldMetadata(alias="lineEndings"),
        pydantic.Field(alias="lineEndings"),
    ]
    rotation: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
