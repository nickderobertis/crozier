

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_polygon_blend_mode import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonBlendMode,
)
from .doc_annotations_list200response_annotations_item_polygon_border_style import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonBorderStyle,
)
from .doc_annotations_list200response_annotations_item_polygon_caption import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonCaption,
)
from .doc_annotations_list200response_annotations_item_polygon_color import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonColor,
)
from .doc_annotations_list200response_annotations_item_polygon_flags import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonFlags,
)
from .doc_annotations_list200response_annotations_item_polygon_identity_quality import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonIdentityQuality,
)
from .doc_annotations_list200response_annotations_item_polygon_in_reply_to import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonInReplyTo,
)
from .doc_annotations_list200response_annotations_item_polygon_intent import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonIntent,
)
from .doc_annotations_list200response_annotations_item_polygon_interior_color import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonInteriorColor,
)
from .doc_annotations_list200response_annotations_item_polygon_measure import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonMeasure,
)
from .doc_annotations_list200response_annotations_item_polygon_page import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonPage,
)
from .doc_annotations_list200response_annotations_item_polygon_rect import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonRect,
)
from .doc_annotations_list200response_annotations_item_polygon_ref import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonRef,
)
from .doc_annotations_list200response_annotations_item_polygon_reply_type import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonReplyType,
)
from .doc_annotations_list200response_annotations_item_polygon_vertices_item import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonVerticesItem,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsList200ResponseAnnotationsItemPolygon(UniversalBaseModel):
    intent: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemPolygonIntent] = None
    measure: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemPolygonMeasure] = None
    caption: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemPolygonCaption] = None
    ref: DocAnnotationsList200ResponseAnnotationsItemPolygonRef
    page: DocAnnotationsList200ResponseAnnotationsItemPolygonPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemPolygonIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsList200ResponseAnnotationsItemPolygonFlags
    rect: DocAnnotationsList200ResponseAnnotationsItemPolygonRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemPolygonBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemPolygonInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemPolygonReplyType],
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
    color: DocAnnotationsList200ResponseAnnotationsItemPolygonColor
    opacity: float
    stroke_width: typing_extensions.Annotated[
        float, FieldMetadata(alias="strokeWidth"), pydantic.Field(alias="strokeWidth")
    ]
    border_style: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemPolygonBorderStyle,
        FieldMetadata(alias="borderStyle"),
        pydantic.Field(alias="borderStyle"),
    ]
    dash_array: typing_extensions.Annotated[
        typing.Optional[typing.List[float]], FieldMetadata(alias="dashArray"), pydantic.Field(alias="dashArray")
    ] = None
    interior_color: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemPolygonInteriorColor],
        FieldMetadata(alias="interiorColor"),
        pydantic.Field(alias="interiorColor"),
    ] = None
    vertices: typing.List[DocAnnotationsList200ResponseAnnotationsItemPolygonVerticesItem]
    rotation: typing.Optional[float] = None
    cloudy_intensity: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="cloudyIntensity"), pydantic.Field(alias="cloudyIntensity")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
