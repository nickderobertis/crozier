

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_strikeout_blend_mode import (
    DocAnnotationsList200ResponseAnnotationsItemStrikeoutBlendMode,
)
from .doc_annotations_list200response_annotations_item_strikeout_color import (
    DocAnnotationsList200ResponseAnnotationsItemStrikeoutColor,
)
from .doc_annotations_list200response_annotations_item_strikeout_flags import (
    DocAnnotationsList200ResponseAnnotationsItemStrikeoutFlags,
)
from .doc_annotations_list200response_annotations_item_strikeout_identity_quality import (
    DocAnnotationsList200ResponseAnnotationsItemStrikeoutIdentityQuality,
)
from .doc_annotations_list200response_annotations_item_strikeout_in_reply_to import (
    DocAnnotationsList200ResponseAnnotationsItemStrikeoutInReplyTo,
)
from .doc_annotations_list200response_annotations_item_strikeout_intent import (
    DocAnnotationsList200ResponseAnnotationsItemStrikeoutIntent,
)
from .doc_annotations_list200response_annotations_item_strikeout_page import (
    DocAnnotationsList200ResponseAnnotationsItemStrikeoutPage,
)
from .doc_annotations_list200response_annotations_item_strikeout_quad_points_item import (
    DocAnnotationsList200ResponseAnnotationsItemStrikeoutQuadPointsItem,
)
from .doc_annotations_list200response_annotations_item_strikeout_rect import (
    DocAnnotationsList200ResponseAnnotationsItemStrikeoutRect,
)
from .doc_annotations_list200response_annotations_item_strikeout_ref import (
    DocAnnotationsList200ResponseAnnotationsItemStrikeoutRef,
)
from .doc_annotations_list200response_annotations_item_strikeout_reply_type import (
    DocAnnotationsList200ResponseAnnotationsItemStrikeoutReplyType,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsList200ResponseAnnotationsItemStrikeout(UniversalBaseModel):
    ref: DocAnnotationsList200ResponseAnnotationsItemStrikeoutRef
    page: DocAnnotationsList200ResponseAnnotationsItemStrikeoutPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemStrikeoutIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsList200ResponseAnnotationsItemStrikeoutFlags
    rect: DocAnnotationsList200ResponseAnnotationsItemStrikeoutRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemStrikeoutBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemStrikeoutInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemStrikeoutReplyType],
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
    color: DocAnnotationsList200ResponseAnnotationsItemStrikeoutColor
    opacity: float
    quad_points: typing_extensions.Annotated[
        typing.List[DocAnnotationsList200ResponseAnnotationsItemStrikeoutQuadPointsItem],
        FieldMetadata(alias="quadPoints"),
        pydantic.Field(alias="quadPoints"),
    ]
    intent: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemStrikeoutIntent] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
