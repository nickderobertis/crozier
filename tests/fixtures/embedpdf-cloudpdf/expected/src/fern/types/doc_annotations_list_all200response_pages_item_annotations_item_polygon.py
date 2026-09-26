

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_polygon_blend_mode import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonBlendMode,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polygon_border_style import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonBorderStyle,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polygon_caption import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonCaption,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polygon_color import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonColor,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polygon_flags import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonFlags,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polygon_identity_quality import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonIdentityQuality,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polygon_in_reply_to import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonInReplyTo,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polygon_intent import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonIntent,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polygon_interior_color import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonInteriorColor,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polygon_measure import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonMeasure,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polygon_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polygon_rect import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonRect,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polygon_ref import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonRef,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polygon_reply_type import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonReplyType,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polygon_vertices_item import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonVerticesItem,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygon(UniversalBaseModel):
    intent: typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonIntent] = None
    measure: typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonMeasure] = None
    caption: typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonCaption] = None
    ref: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonRef
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonFlags
    rect: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonReplyType],
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
    color: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonColor
    opacity: float
    stroke_width: typing_extensions.Annotated[
        float, FieldMetadata(alias="strokeWidth"), pydantic.Field(alias="strokeWidth")
    ]
    border_style: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonBorderStyle,
        FieldMetadata(alias="borderStyle"),
        pydantic.Field(alias="borderStyle"),
    ]
    dash_array: typing_extensions.Annotated[
        typing.Optional[typing.List[float]], FieldMetadata(alias="dashArray"), pydantic.Field(alias="dashArray")
    ] = None
    interior_color: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonInteriorColor],
        FieldMetadata(alias="interiorColor"),
        pydantic.Field(alias="interiorColor"),
    ] = None
    vertices: typing.List[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonVerticesItem]
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
