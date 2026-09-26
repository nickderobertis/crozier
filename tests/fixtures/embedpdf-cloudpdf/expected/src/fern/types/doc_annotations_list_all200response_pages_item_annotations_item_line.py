

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_line_blend_mode import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineBlendMode,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_line_border_style import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineBorderStyle,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_line_caption import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineCaption,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_line_color import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineColor,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_line_flags import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineFlags,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_line_identity_quality import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineIdentityQuality,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_line_in_reply_to import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineInReplyTo,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_line_intent import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineIntent,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_line_interior_color import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineInteriorColor,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_line_leader import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineLeader,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_line_line_endings import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineLineEndings,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_line_line_points import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineLinePoints,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_line_measure import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasure,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_line_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinePage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_line_rect import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineRect,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_line_ref import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineRef,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_line_reply_type import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineReplyType,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLine(UniversalBaseModel):
    intent: typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineIntent] = None
    measure: typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasure] = None
    caption: typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineCaption] = None
    leader: typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineLeader] = None
    ref: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineRef
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinePage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineFlags
    rect: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineReplyType],
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
    color: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineColor
    opacity: float
    stroke_width: typing_extensions.Annotated[
        float, FieldMetadata(alias="strokeWidth"), pydantic.Field(alias="strokeWidth")
    ]
    border_style: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineBorderStyle,
        FieldMetadata(alias="borderStyle"),
        pydantic.Field(alias="borderStyle"),
    ]
    dash_array: typing_extensions.Annotated[
        typing.Optional[typing.List[float]], FieldMetadata(alias="dashArray"), pydantic.Field(alias="dashArray")
    ] = None
    interior_color: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineInteriorColor],
        FieldMetadata(alias="interiorColor"),
        pydantic.Field(alias="interiorColor"),
    ] = None
    line_points: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineLinePoints,
        FieldMetadata(alias="linePoints"),
        pydantic.Field(alias="linePoints"),
    ]
    line_endings: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineLineEndings,
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
