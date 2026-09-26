

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_square_blend_mode import (
    DocAnnotationsList200ResponseAnnotationsItemSquareBlendMode,
)
from .doc_annotations_list200response_annotations_item_square_border_style import (
    DocAnnotationsList200ResponseAnnotationsItemSquareBorderStyle,
)
from .doc_annotations_list200response_annotations_item_square_color import (
    DocAnnotationsList200ResponseAnnotationsItemSquareColor,
)
from .doc_annotations_list200response_annotations_item_square_flags import (
    DocAnnotationsList200ResponseAnnotationsItemSquareFlags,
)
from .doc_annotations_list200response_annotations_item_square_identity_quality import (
    DocAnnotationsList200ResponseAnnotationsItemSquareIdentityQuality,
)
from .doc_annotations_list200response_annotations_item_square_in_reply_to import (
    DocAnnotationsList200ResponseAnnotationsItemSquareInReplyTo,
)
from .doc_annotations_list200response_annotations_item_square_interior_color import (
    DocAnnotationsList200ResponseAnnotationsItemSquareInteriorColor,
)
from .doc_annotations_list200response_annotations_item_square_page import (
    DocAnnotationsList200ResponseAnnotationsItemSquarePage,
)
from .doc_annotations_list200response_annotations_item_square_rect import (
    DocAnnotationsList200ResponseAnnotationsItemSquareRect,
)
from .doc_annotations_list200response_annotations_item_square_rect_differences import (
    DocAnnotationsList200ResponseAnnotationsItemSquareRectDifferences,
)
from .doc_annotations_list200response_annotations_item_square_ref import (
    DocAnnotationsList200ResponseAnnotationsItemSquareRef,
)
from .doc_annotations_list200response_annotations_item_square_reply_type import (
    DocAnnotationsList200ResponseAnnotationsItemSquareReplyType,
)
from .doc_annotations_list200response_annotations_item_square_unrotated_rect import (
    DocAnnotationsList200ResponseAnnotationsItemSquareUnrotatedRect,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsList200ResponseAnnotationsItemSquare(UniversalBaseModel):
    ref: DocAnnotationsList200ResponseAnnotationsItemSquareRef
    page: DocAnnotationsList200ResponseAnnotationsItemSquarePage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemSquareIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsList200ResponseAnnotationsItemSquareFlags
    rect: DocAnnotationsList200ResponseAnnotationsItemSquareRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemSquareBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemSquareInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemSquareReplyType],
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
    color: DocAnnotationsList200ResponseAnnotationsItemSquareColor
    opacity: float
    stroke_width: typing_extensions.Annotated[
        float, FieldMetadata(alias="strokeWidth"), pydantic.Field(alias="strokeWidth")
    ]
    border_style: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemSquareBorderStyle,
        FieldMetadata(alias="borderStyle"),
        pydantic.Field(alias="borderStyle"),
    ]
    dash_array: typing_extensions.Annotated[
        typing.Optional[typing.List[float]], FieldMetadata(alias="dashArray"), pydantic.Field(alias="dashArray")
    ] = None
    interior_color: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemSquareInteriorColor],
        FieldMetadata(alias="interiorColor"),
        pydantic.Field(alias="interiorColor"),
    ] = None
    cloudy_intensity: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="cloudyIntensity"), pydantic.Field(alias="cloudyIntensity")
    ] = None
    rect_differences: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemSquareRectDifferences],
        FieldMetadata(alias="rectDifferences"),
        pydantic.Field(alias="rectDifferences"),
    ] = None
    rotation: typing.Optional[float] = None
    unrotated_rect: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemSquareUnrotatedRect],
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
