

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_square_blend_mode import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareBlendMode,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_square_border_style import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareBorderStyle,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_square_color import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareColor,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_square_flags import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareFlags,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_square_identity_quality import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareIdentityQuality,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_square_in_reply_to import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareInReplyTo,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_square_interior_color import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareInteriorColor,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_square_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquarePage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_square_rect import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareRect,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_square_rect_differences import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareRectDifferences,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_square_ref import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareRef,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_square_reply_type import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareReplyType,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_square_unrotated_rect import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareUnrotatedRect,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquare(UniversalBaseModel):
    ref: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareRef
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquarePage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareFlags
    rect: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareReplyType],
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
    color: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareColor
    opacity: float
    stroke_width: typing_extensions.Annotated[
        float, FieldMetadata(alias="strokeWidth"), pydantic.Field(alias="strokeWidth")
    ]
    border_style: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareBorderStyle,
        FieldMetadata(alias="borderStyle"),
        pydantic.Field(alias="borderStyle"),
    ]
    dash_array: typing_extensions.Annotated[
        typing.Optional[typing.List[float]], FieldMetadata(alias="dashArray"), pydantic.Field(alias="dashArray")
    ] = None
    interior_color: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareInteriorColor],
        FieldMetadata(alias="interiorColor"),
        pydantic.Field(alias="interiorColor"),
    ] = None
    cloudy_intensity: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="cloudyIntensity"), pydantic.Field(alias="cloudyIntensity")
    ] = None
    rect_differences: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareRectDifferences],
        FieldMetadata(alias="rectDifferences"),
        pydantic.Field(alias="rectDifferences"),
    ] = None
    rotation: typing.Optional[float] = None
    unrotated_rect: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquareUnrotatedRect],
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
