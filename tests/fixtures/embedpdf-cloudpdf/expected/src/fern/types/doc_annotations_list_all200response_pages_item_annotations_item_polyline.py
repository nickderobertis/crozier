

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_polyline_blend_mode import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineBlendMode,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polyline_border_style import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineBorderStyle,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polyline_caption import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineCaption,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polyline_color import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineColor,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polyline_flags import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineFlags,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polyline_identity_quality import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineIdentityQuality,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polyline_in_reply_to import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineInReplyTo,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polyline_intent import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineIntent,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polyline_interior_color import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineInteriorColor,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polyline_line_endings import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineLineEndings,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polyline_measure import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineMeasure,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polyline_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylinePage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polyline_rect import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineRect,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polyline_ref import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineRef,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polyline_reply_type import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineReplyType,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polyline_vertices_item import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineVerticesItem,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolyline(UniversalBaseModel):
    intent: typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineIntent] = None
    measure: typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineMeasure] = None
    caption: typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineCaption] = None
    ref: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineRef
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylinePage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineFlags
    rect: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineReplyType],
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
    color: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineColor
    opacity: float
    stroke_width: typing_extensions.Annotated[
        float, FieldMetadata(alias="strokeWidth"), pydantic.Field(alias="strokeWidth")
    ]
    border_style: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineBorderStyle,
        FieldMetadata(alias="borderStyle"),
        pydantic.Field(alias="borderStyle"),
    ]
    dash_array: typing_extensions.Annotated[
        typing.Optional[typing.List[float]], FieldMetadata(alias="dashArray"), pydantic.Field(alias="dashArray")
    ] = None
    interior_color: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineInteriorColor],
        FieldMetadata(alias="interiorColor"),
        pydantic.Field(alias="interiorColor"),
    ] = None
    vertices: typing.List[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineVerticesItem]
    rotation: typing.Optional[float] = None
    line_endings: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineLineEndings,
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
