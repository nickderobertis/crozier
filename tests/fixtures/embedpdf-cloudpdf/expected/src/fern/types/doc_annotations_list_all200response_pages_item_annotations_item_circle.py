

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_circle_blend_mode import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleBlendMode,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_circle_border_style import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleBorderStyle,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_circle_color import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleColor,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_circle_flags import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleFlags,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_circle_identity_quality import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleIdentityQuality,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_circle_in_reply_to import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleInReplyTo,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_circle_interior_color import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleInteriorColor,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_circle_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCirclePage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_circle_rect import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleRect,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_circle_rect_differences import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleRectDifferences,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_circle_ref import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleRef,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_circle_reply_type import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleReplyType,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_circle_unrotated_rect import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleUnrotatedRect,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircle(UniversalBaseModel):
    ref: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleRef
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCirclePage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleFlags
    rect: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleReplyType],
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
    color: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleColor
    opacity: float
    stroke_width: typing_extensions.Annotated[
        float, FieldMetadata(alias="strokeWidth"), pydantic.Field(alias="strokeWidth")
    ]
    border_style: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleBorderStyle,
        FieldMetadata(alias="borderStyle"),
        pydantic.Field(alias="borderStyle"),
    ]
    dash_array: typing_extensions.Annotated[
        typing.Optional[typing.List[float]], FieldMetadata(alias="dashArray"), pydantic.Field(alias="dashArray")
    ] = None
    interior_color: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleInteriorColor],
        FieldMetadata(alias="interiorColor"),
        pydantic.Field(alias="interiorColor"),
    ] = None
    cloudy_intensity: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="cloudyIntensity"), pydantic.Field(alias="cloudyIntensity")
    ] = None
    rect_differences: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleRectDifferences],
        FieldMetadata(alias="rectDifferences"),
        pydantic.Field(alias="rectDifferences"),
    ] = None
    rotation: typing.Optional[float] = None
    unrotated_rect: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemCircleUnrotatedRect],
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
