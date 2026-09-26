

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_circle_blend_mode import (
    DocAnnotationsList200ResponseAnnotationsItemCircleBlendMode,
)
from .doc_annotations_list200response_annotations_item_circle_border_style import (
    DocAnnotationsList200ResponseAnnotationsItemCircleBorderStyle,
)
from .doc_annotations_list200response_annotations_item_circle_color import (
    DocAnnotationsList200ResponseAnnotationsItemCircleColor,
)
from .doc_annotations_list200response_annotations_item_circle_flags import (
    DocAnnotationsList200ResponseAnnotationsItemCircleFlags,
)
from .doc_annotations_list200response_annotations_item_circle_identity_quality import (
    DocAnnotationsList200ResponseAnnotationsItemCircleIdentityQuality,
)
from .doc_annotations_list200response_annotations_item_circle_in_reply_to import (
    DocAnnotationsList200ResponseAnnotationsItemCircleInReplyTo,
)
from .doc_annotations_list200response_annotations_item_circle_interior_color import (
    DocAnnotationsList200ResponseAnnotationsItemCircleInteriorColor,
)
from .doc_annotations_list200response_annotations_item_circle_page import (
    DocAnnotationsList200ResponseAnnotationsItemCirclePage,
)
from .doc_annotations_list200response_annotations_item_circle_rect import (
    DocAnnotationsList200ResponseAnnotationsItemCircleRect,
)
from .doc_annotations_list200response_annotations_item_circle_rect_differences import (
    DocAnnotationsList200ResponseAnnotationsItemCircleRectDifferences,
)
from .doc_annotations_list200response_annotations_item_circle_ref import (
    DocAnnotationsList200ResponseAnnotationsItemCircleRef,
)
from .doc_annotations_list200response_annotations_item_circle_reply_type import (
    DocAnnotationsList200ResponseAnnotationsItemCircleReplyType,
)
from .doc_annotations_list200response_annotations_item_circle_unrotated_rect import (
    DocAnnotationsList200ResponseAnnotationsItemCircleUnrotatedRect,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsList200ResponseAnnotationsItemCircle(UniversalBaseModel):
    ref: DocAnnotationsList200ResponseAnnotationsItemCircleRef
    page: DocAnnotationsList200ResponseAnnotationsItemCirclePage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemCircleIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsList200ResponseAnnotationsItemCircleFlags
    rect: DocAnnotationsList200ResponseAnnotationsItemCircleRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemCircleBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemCircleInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemCircleReplyType],
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
    color: DocAnnotationsList200ResponseAnnotationsItemCircleColor
    opacity: float
    stroke_width: typing_extensions.Annotated[
        float, FieldMetadata(alias="strokeWidth"), pydantic.Field(alias="strokeWidth")
    ]
    border_style: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemCircleBorderStyle,
        FieldMetadata(alias="borderStyle"),
        pydantic.Field(alias="borderStyle"),
    ]
    dash_array: typing_extensions.Annotated[
        typing.Optional[typing.List[float]], FieldMetadata(alias="dashArray"), pydantic.Field(alias="dashArray")
    ] = None
    interior_color: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemCircleInteriorColor],
        FieldMetadata(alias="interiorColor"),
        pydantic.Field(alias="interiorColor"),
    ] = None
    cloudy_intensity: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="cloudyIntensity"), pydantic.Field(alias="cloudyIntensity")
    ] = None
    rect_differences: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemCircleRectDifferences],
        FieldMetadata(alias="rectDifferences"),
        pydantic.Field(alias="rectDifferences"),
    ] = None
    rotation: typing.Optional[float] = None
    unrotated_rect: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemCircleUnrotatedRect],
        FieldMetadata(alias="unrotatedRect"),
        pydantic.Field(alias="unrotatedRect"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
