

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_strikeout_blend_mode import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutBlendMode,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_strikeout_color import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutColor,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_strikeout_flags import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutFlags,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_strikeout_identity_quality import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutIdentityQuality,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_strikeout_in_reply_to import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutInReplyTo,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_strikeout_intent import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutIntent,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_strikeout_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_strikeout_quad_points_item import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutQuadPointsItem,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_strikeout_rect import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutRect,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_strikeout_ref import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutRef,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_strikeout_reply_type import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutReplyType,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeout(UniversalBaseModel):
    ref: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutRef
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutFlags
    rect: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutReplyType],
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
    color: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutColor
    opacity: float
    quad_points: typing_extensions.Annotated[
        typing.List[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutQuadPointsItem],
        FieldMetadata(alias="quadPoints"),
        pydantic.Field(alias="quadPoints"),
    ]
    intent: typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutIntent] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
