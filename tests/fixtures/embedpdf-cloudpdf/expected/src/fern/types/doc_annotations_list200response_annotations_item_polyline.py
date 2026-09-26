

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_polyline_blend_mode import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineBlendMode,
)
from .doc_annotations_list200response_annotations_item_polyline_border_style import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineBorderStyle,
)
from .doc_annotations_list200response_annotations_item_polyline_caption import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineCaption,
)
from .doc_annotations_list200response_annotations_item_polyline_color import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineColor,
)
from .doc_annotations_list200response_annotations_item_polyline_flags import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineFlags,
)
from .doc_annotations_list200response_annotations_item_polyline_identity_quality import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineIdentityQuality,
)
from .doc_annotations_list200response_annotations_item_polyline_in_reply_to import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineInReplyTo,
)
from .doc_annotations_list200response_annotations_item_polyline_intent import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineIntent,
)
from .doc_annotations_list200response_annotations_item_polyline_interior_color import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineInteriorColor,
)
from .doc_annotations_list200response_annotations_item_polyline_line_endings import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineLineEndings,
)
from .doc_annotations_list200response_annotations_item_polyline_measure import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineMeasure,
)
from .doc_annotations_list200response_annotations_item_polyline_page import (
    DocAnnotationsList200ResponseAnnotationsItemPolylinePage,
)
from .doc_annotations_list200response_annotations_item_polyline_rect import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineRect,
)
from .doc_annotations_list200response_annotations_item_polyline_ref import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineRef,
)
from .doc_annotations_list200response_annotations_item_polyline_reply_type import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineReplyType,
)
from .doc_annotations_list200response_annotations_item_polyline_vertices_item import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineVerticesItem,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsList200ResponseAnnotationsItemPolyline(UniversalBaseModel):
    intent: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemPolylineIntent] = None
    measure: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemPolylineMeasure] = None
    caption: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemPolylineCaption] = None
    ref: DocAnnotationsList200ResponseAnnotationsItemPolylineRef
    page: DocAnnotationsList200ResponseAnnotationsItemPolylinePage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemPolylineIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsList200ResponseAnnotationsItemPolylineFlags
    rect: DocAnnotationsList200ResponseAnnotationsItemPolylineRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemPolylineBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemPolylineInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemPolylineReplyType],
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
    color: DocAnnotationsList200ResponseAnnotationsItemPolylineColor
    opacity: float
    stroke_width: typing_extensions.Annotated[
        float, FieldMetadata(alias="strokeWidth"), pydantic.Field(alias="strokeWidth")
    ]
    border_style: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemPolylineBorderStyle,
        FieldMetadata(alias="borderStyle"),
        pydantic.Field(alias="borderStyle"),
    ]
    dash_array: typing_extensions.Annotated[
        typing.Optional[typing.List[float]], FieldMetadata(alias="dashArray"), pydantic.Field(alias="dashArray")
    ] = None
    interior_color: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemPolylineInteriorColor],
        FieldMetadata(alias="interiorColor"),
        pydantic.Field(alias="interiorColor"),
    ] = None
    vertices: typing.List[DocAnnotationsList200ResponseAnnotationsItemPolylineVerticesItem]
    rotation: typing.Optional[float] = None
    line_endings: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemPolylineLineEndings,
        FieldMetadata(alias="lineEndings"),
        pydantic.Field(alias="lineEndings"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
